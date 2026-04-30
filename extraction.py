from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
loader=PDFPlumberLoader("sem620(syllabus).pdf")
data=loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50,
    separators=["\n\n","\n","|"," "," "]
    )
docs = text_splitter.split_documents(data)
print (docs)

for i, doc in enumerate(docs):
    print(f"\nChunk {i+1}:")
    print(doc.page_content)
    print("---")

print(f"\nTotal chunks:{len(docs)}")
