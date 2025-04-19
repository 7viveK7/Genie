from fastapi import FastAPI
from app.routes.upload import upload_router
from app.routes.health import health
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporary for debugging
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/cors-test")
async def cors_test():
    return {"message": "CORS test successful"}

app.include_router(upload_router)
app.include_router(health)



@app.get("/")
def home():
    return {"message": "Welcome to HIREGENIUS"}