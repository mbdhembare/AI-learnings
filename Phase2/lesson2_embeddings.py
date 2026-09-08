from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The car is very fast.",
    "The automobile is very quick.",
    "I like eating pizza."
]

embeddings = model.encode(sentences)

similarity = cosine_similarity(embeddings)

print("Cosine Similarity Matrix:")
print(similarity)