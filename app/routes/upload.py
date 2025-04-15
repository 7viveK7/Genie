from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services import pdf_utils ,embedding_engine,gpt_feedback,similarity_engine,storage

import logging
from typing import Dict, Any
from app.models.response_model import MatchResponse

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

upload_router = APIRouter()

@upload_router.post("/upload-resume/", response_model=MatchResponse)
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

        # 2. Generate embedding_engines
        resume_embedding = embedding_engine.embed_text(resume_text)  # Fixed: use embedding_engine
        logger.info("Resume embedded")

        jd_embedding = embedding_engine.embed_text(job_description)  # Fixed: use embedding_engine
        logger.info("JD embedded")

        # 3. Store in ChromaDB
        storage.store_embeddings(  # Fixed: use storage
            embedding=resume_embedding,
            metadata={"id": file.filename}
        )
        logger.info("Stored in ChromaDB")

        # 4. Calculate similarity
        relevance_score = similarity_engine.cosine_similarity(  # Fixed: use similarity
            resume_embedding,
            jd_embedding
        )
        logger.info(f"similarity_engine calculated: {relevance_score}")

        missing_skills = similarity_engine.extract_missing_skills(resume_text, job_description)

        # 5. Generate GPT summary
        summary_dict = gpt_feedback.generate_summary(
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
