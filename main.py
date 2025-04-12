from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from utils import (
    pdf_utils,
    embeddings,
    similarity,
    storage,
    gpt_utils
)
from schemas.models import MatchResponse
import json  # Missing import
from typing import Dict, Any  # For type hints
import traceback  # For error handling

app = FastAPI()

@app.post("/upload-resume/", response_model=MatchResponse)
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
) -> Dict[str, Any]:
    try:
        # 1. Read and extract PDF
        content = await file.read()
        print("File read successfully")
        
        resume_text = pdf_utils.extract_text_from_pdf(content)  # Fixed: use pdf_utils
        print("PDF extracted")
        
        # 2. Generate embeddings
        resume_embedding = embeddings.embed_text(resume_text)  # Fixed: use embeddings
        print("Resume embedded")
        
        jd_embedding = embeddings.embed_text(job_description)  # Fixed: use embeddings
        print("JD embedded")
        
        # 3. Store in ChromaDB
        storage.store_embeddings(  # Fixed: use storage
            embedding=resume_embedding,
            metadata={"id": file.filename}
        )
        print("Stored in ChromaDB")
        
        # 4. Calculate similarity
        relevance_score = similarity.cosine_similarity(  # Fixed: use similarity
            resume_embedding,
            jd_embedding
        )
        print(f"Similarity calculated: {relevance_score}")
        missing_skills = similarity.extract_missing_skills(resume_text, job_description)

        # 5. Generate GPT summary
        summary_dict = gpt_utils.generate_summary(  # Fixed: use gpt_utils
         resume=resume_text,
         job_description=job_description,
         relevance_score=relevance_score,
         missing_skills=missing_skills,
         filename=file.filename

        )

        print("GPT summary generated")
        
        # 6. Return response
        return {
            "filename": file.filename,
            "relevance_score": round(relevance_score, 2),
            **summary_dict
        }
        
 
    except Exception as e:
        print("FULL TRACEBACK:")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Error processing resume: {str(e)}"
        )