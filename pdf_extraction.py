import pdfplumber
import re                          # ← ADD THIS

def pdf_to_string(file_path):
    all_text = ""
    with pdfplumber.open(file_path) as pdf:   # ← use the parameter, not hardcoded string
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text += text + "\n"
    return all_text

def clean_text(text):
    text = text.replace("\x00", "").replace("\x0c", "")
    text = text.replace("\xa0", " ").replace("\u200b", "")
    text = re.sub(r'-\n(\w)', r'\1', text)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(lines)
    return text.strip()


my_text_string = pdf_to_string("sem620(syllabus).pdf")

cleaned_text = clean_text(my_text_string)    

words = cleaned_text.split()
first_500 = " ".join(words[:500])

print(first_500 + "\n")                     