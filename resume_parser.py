# resume_parser.py

import pdfplumber
import re
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Sample skill set
SKILL_SET = {
    'python', 'java', 'sql', 'excel', 'machine learning', 'deep learning',
    'data analysis', 'django', 'flask', 'react', 'html', 'css', 'javascript',
    'pandas', 'numpy', 'power bi', 'tableau', 'nlp', 'git', 'aws', 'c++'
}

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.lower()

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group() if match else ""

def extract_phone(text):
    pattern = r'\+?\d{1,3}?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
    match = re.search(pattern, text)
    return match.group() if match else ""

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return ""

def extract_skills(text):
    return list({skill for skill in SKILL_SET if skill.lower() in text})

def parse_resume(file):
    text = extract_text_from_pdf(file)
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "raw_text": text
    }
