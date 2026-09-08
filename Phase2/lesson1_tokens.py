import tiktoken

embedings=tiktoken.get_encoding("cl100k_base")

sentences = [
    "Hello",
    "Hello world",
    "Generative AI",
    "I am learning Generative AI",
    "The server is running slowly.",
    "def calculate_average(numbers): return sum(numbers) / len(numbers)"
]

for sentence in sentences:
    token=embedings.encode(sentence)

    print("\ntext: ", sentence)
    print("words count: ", len(sentence.split()))
    print("token count: ", len(token))
    print("tokens: ", )
    for token in token:
        print(token, "->", embedings.decode([token]))
