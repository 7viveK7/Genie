from fastapi import FastAPI
from app.routes.upload import upload_router
from app.routes.health import health
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://genie-rho.vercel.app/",       
        "https://genie-1-vqcr.onrender.com/",  
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(health)



@app.get("/")
def home():
    return {"message": "Welcome to HIREGENIUS"}