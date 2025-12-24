# src/loader.py
from PyPDF2 import PdfReader
from pathlib import Path

def load_documents(folder="data/docs"):
    docs = []
    for file in Path(folder).glob("*"):
        if file.suffix.lower() == ".pdf":
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        elif file.suffix.lower() == ".txt":
            text = file.read_text(encoding="utf-8", errors="ignore")
        else:
            continue

        docs.append({
            "name": file.name,
            "text": text.strip()
        })
    return docs
