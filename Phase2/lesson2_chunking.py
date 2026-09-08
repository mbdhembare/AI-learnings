text = """
The payment service experienced high latency.
The database connection pool reached its maximum capacity.
Several queries were running for a long time.
The application team increased the connection pool size.
They also optimized the slow database queries.
"""

chunk_size=100

chunks=[]

for i in range(0, len(text), chunk_size):
    chunk=text[i:i+chunk_size]
    chunks.append(chunk)

for index, chunk in enumerate(chunks):
    print(f"\n---chunk {index+1}----")
    print(chunk)