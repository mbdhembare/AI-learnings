from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "How to reset your password",
    "How to configure database connections",
    "How to troubleshoot high CPU usage",
    "How to investigate API latency",
    "How to create a new user account"
]

query = "Why is my API response very slow?"

document_embeddings = model.encode(documents)
query_embedding = model.encode([query])

similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

for document, score in zip(documents, similarities):
    print(f"{score:.4f} -> {document}")