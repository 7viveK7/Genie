# main.py
from fastapi import FastAPI
import pdfplumber

from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()  # Looks for .env in the same directory

app = FastAPI()

openai_key = os.getenv("OPENAI_API_KEY")  # Access the key

app = FastAPI()  # <-- This must be named `app`

@app.get("/extract-text")
async def extract_text():
    text = ""
    with pdfplumber.open("./vivekananda_resume.pdf") as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return {"text": openai_key, "extracted_text": text}