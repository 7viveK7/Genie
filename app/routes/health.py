from fastapi import APIRouter, UploadFile, File, Form, HTTPException

health = APIRouter()

@health.get("/health")
def health_check():
    return {"status": "alive"}
    