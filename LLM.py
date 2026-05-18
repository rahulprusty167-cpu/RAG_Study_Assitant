from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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"
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant that answers questions about the course syllabus.

Context: {context}
Question: {question}
""")

chain = prompt | llm


while True:
    question = input("\nAsk a question (or type 'exit' to quit): ")
    
    if question.lower() == "exit":
        print("Goodbye!")
        break
    
    response = chain.invoke({
        "context": "The syllabus of Computer Networks includes topics such as network architecture, protocols, and security.",
        "question": question
    })
    
    print("\nAnswer:", response.content)