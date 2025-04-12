# # main.py
# from fastapi import FastAPI
# import pdfplumber

# from fastapi import FastAPI
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()  # Looks for .env in the same directory

# app = FastAPI()

# openai_key = os.getenv("OPENAI_API_KEY")  # Access the key

# app = FastAPI()  # <-- This must be named `app`

# @app.get("/extract-text")
# async def extract_text():
#     text = ""
#     with pdfplumber.open("./vivekananda_resume.pdf") as pdf:
#         for page in pdf.pages:
#             text += page.extract_text()
#     return {"text": openai_key, "extracted_text": text}

from fastapi import FastAPI, UploadFile, File
import pdfplumber
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to HIREGENIUS"}

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()

    # Use pdfplumber to extract text
    text = ""
    with pdfplumber.open(io.BytesIO(content)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    # Optional: Print the text in console
    print("📄 Extracted Resume Text:\n", text)

    return {
        "filename": file.filename,
        "size": len(content),
        "preview": text[:300]  # send only the first 300 chars as a preview
    }

