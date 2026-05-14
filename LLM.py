from langchain_groq import ChatGroq         
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key="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"
)
                 
prompt = ChatPromptTemplate.from_template("""             
You are a helpful assistant that answers questions about the course syllabus.

Context: {context}
Question: {question}
""")                                                      

chain = prompt | llm                                     

response = chain.invoke({
    "context": "The syllabus of Computer Networks includes topics such as network architecture, protocols, and security.",
    "question": "What is the syllabus of Computer Networks?"  # ✅ lowercase keys match template
})

print(response)