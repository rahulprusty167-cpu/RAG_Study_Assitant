from langchain_community.document_loaders import PDFPlumberLoader # Loading PdfPlumber to Load the PDF file
from langchain_text_splitters import RecursiveCharacterTextSplitter # Importing RecursiveCharacterTextSplitter to split the text into chunks
loader=PDFPlumberLoader("sem620(syllabus).pdf")
data=loader.load()

text_splitter = RecursiveCharacterTextSplitter(       # Initialize text splitter with parameters
    chunk_size=500, 
    chunk_overlap=50,
    separators=["\n\n","\n","|"," "," "]        
    )
docs = text_splitter.split_documents(data)

if __name__ == "__main__":
 print (docs)

for i, doc in enumerate(docs):   #Printing the chunks of text
    print(f"\nChunk {i+1}:")
    print(doc.page_content)
    print("---")

print(f"\nTotal chunks:{len(docs)}")  # Printing the total number of chunks created
