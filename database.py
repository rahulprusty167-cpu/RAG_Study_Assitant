#Impoerting necessary libraries and modules for the database operations
import chromadb 
from chromadb import EmbeddingFunction, Documents, Embeddings
from extraction import docs 
from Embeding import embeddings

# Wrap your embeddings in ChromaDB's required format
class MyEmbeddingFunction(EmbeddingFunction):

    def __init__(self):
        pass
    def __call__(self, input: Documents) -> Embeddings:
        return embeddings.embed_documents(input)  

client = chromadb.PersistentClient(path="./db")

#Collection is a container for your documeents for the embeddings
collections = client.get_or_create_collection(
    name="course_data",
    embedding_function=MyEmbeddingFunction()
)

# Prepare your documents, ids, and metadatas for insertion into the collection
documents = [d.page_content for d in docs]        
ids = [f"doc{i}" for i in range(len(docs))]        
metadatas = [d.metadata for d in docs]            

#Adding the documents, ids, and metadatas to the collection in the ChromaDB database
collections.add(
    documents=documents,
    ids=ids,
    metadatas=metadatas
)

print("The number of data stored are:", collections.count())