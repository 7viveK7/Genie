import chromadb
from chromadb.config import Settings
from config import Config

def get_chroma_client():
    # New recommended client configuration
    return chromadb.PersistentClient(
        path=Config.CHROMA_DB_PATH,
        settings=Settings(
            allow_reset=True,
            anonymized_telemetry=False  # Disable if you don't want telemetry
        )
    )

def get_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(
        name="resumes",
        metadata={"hnsw:space": "cosine"}  # Optional: specify similarity metric
    )

def store_embeddings(embedding, metadata: dict):
    """Store embeddings in ChromaDB"""
    collection = get_collection()
    collection.add(
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[metadata["id"]]
    )