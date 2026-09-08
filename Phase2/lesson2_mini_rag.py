from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Our knowledge base
documents = [
    "To reset your password, open the login page and select Forgot Password.",
    "High CPU usage can be caused by memory pressure or intensive application processing.",
    "API latency can increase because of slow database queries or network problems.",
    "Database connection pool exhaustion can cause application requests to become slow.",
    "Expired authentication tokens can cause API requests to fail."
]

# 3. Create embeddings for documents
document_embeddings=model.encode(documents)

# 4. User question
query = "Why is my application API responding very slowly?"

# 5. Create embedding for the question
query_embedding=model.encode([query])

# 6. Calculate similarity
similarities=cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

# 7. Find the most relevant documents
results= sorted(
    zip(documents, similarities),
    key=lambda x: x[1],
    reverse=True
)

# 8. Display results
print("\nQuery:")
print(query)

print("\nRetrieved documents:")

for document, score in results[:3]:
    print(f"\nScore: {score:.4f}")
    print(document)