sentences = [
    "Hello world!",
    "The server is running slowly.",
    "I am learning Generative AI.",
    "Tokenization is important for LLMs."
]

for sentence in sentences:
    words=sentence.split()
    print(words)
    print(sentence)
    print(len(words))