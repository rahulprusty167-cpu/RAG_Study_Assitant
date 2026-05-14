from extraction  import docs
#Loading HuggingFaceEmbeddings to create embeddings for the text data
from langchain_huggingface import HuggingFaceEmbeddings 
# Importing SentenceTransformer to create embeddings for the text data
from sentence_transformers import SentenceTransformer 

#Loading the pre-trained model "all-MiniLM-L6-v2" from HuggingFace to create embeddings for the text data
embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2") 

# Creating an embedding for the query "What is the course name" to test if the embeddings are working correctly
test = embeddings.embed_query("What is the course name") 
# Printing the length of the embedding vector to verify that the embeddings are working correctly  
print(f"Embedding vector length: {len(test)}")
print("Embeddings working correctly!") 