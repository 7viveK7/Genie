from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from utils import (
    pdf_utils,
    embeddings,
    similarity,
    storage,
    gpt_utils
)
import logging
from typing import Dict, Any
from schemas.models import MatchResponse

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/upload-resume/", response_model=MatchResponse)
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
) -> Dict[str, Any]:
    try:
        logger.info("Resume upload started: %s", file.filename)
        
        # 1. Read and extract PDF
        content = await file.read()
        logger.info("File read successfully")
        
        resume_text = pdf_utils.extract_text_from_pdf(content)  # Fixed: use pdf_utils
        logger.info("PDF extracted")

        # 2. Generate embeddings
        resume_embedding = embeddings.embed_text(resume_text)  # Fixed: use embeddings
        logger.info("Resume embedded")

        jd_embedding = embeddings.embed_text(job_description)  # Fixed: use embeddings
        logger.info("JD embedded")

        # 3. Store in ChromaDB
        storage.store_embeddings(  # Fixed: use storage
            embedding=resume_embedding,
            metadata={"id": file.filename}
        )
        logger.info("Stored in ChromaDB")

        # 4. Calculate similarity
        relevance_score = similarity.cosine_similarity(  # Fixed: use similarity
            resume_embedding,
            jd_embedding
        )
        logger.info(f"Similarity calculated: {relevance_score}")

        missing_skills = similarity.extract_missing_skills(resume_text, job_description)

        # 5. Generate GPT summary
        summary_dict = gpt_utils.generate_summary(
            resume_text,
            job_description,
            missing_skills=missing_skills,
            relevance_score=relevance_score,
            filename=file.filename
        )

        logger.info("GPT summary generated")
        
        # 6. Return response
        return { **summary_dict }

    except Exception as e:
        logger.error(f"Error in upload_resume: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error processing resume: {str(e)}"
        )
