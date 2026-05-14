import chromadb
from chromadb import EmbeddingFunction, Documents, Embeddings
from extraction import docs
from Embeding import embeddings

class MyEmbeddingFunction(EmbeddingFunction):

    def __init__(self):
        pass
    def __call__(self, input: Documents) -> Embeddings:
        return embeddings.embed_documents(input)  

client = chromadb.PersistentClient(path="./db")

collections = client.get_or_create_collection(
    name="course_data",
    embedding_function=MyEmbeddingFunction()
)

def retrieve(query, top_k=5):
    results = collections.query(
        query_texts=[query],
        n_results=top_k
    )
    return results['documents'][0], results['metadatas'][0]

chunks = retrieve("What is the syllabus of Computer Networks?")
for chunk in chunks:
    print(chunk)