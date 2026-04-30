from extraction  import doc
from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import sentence_transformer

embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

test = embeddings.embed_query("What is the course name")
print(f"Embedding vector length: {len(test)}")  
print("Embeddings working correctly!")