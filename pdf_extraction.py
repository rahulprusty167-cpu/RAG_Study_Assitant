import pdfplumber

def pdf_to_string(file_path):
    all_text=""

    with pdfplumber.open("sem620(syllabus).pdf ")as pdf:
        for page in pdf.pages:
         text = page.extract_text()
         if text:
            all_text += text + "\n"
        
        return all_text
    

my_text_string = pdf_to_string("sem620(syllabus).pdf")
words = my_text_string.split()
first_500 = " ".join(words[:500])
print(first_500 + "\n" )