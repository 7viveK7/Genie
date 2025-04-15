# import chromadb
# from chromadb.config import Settings
# from app.config.settings import settings  # assuming settings.py has CHROMA_DB_PATH

# def get_chroma_client():
#     return chromadb.PersistentClient(
#         path=settings.CHROMA_DB_PATH,
#         settings=Settings(
#             allow_reset=True,
#             anonymized_telemetry=False
#         )
#     )

# def get_collection():
#     client = get_chroma_client()
#     return client.get_or_create_collection(
#         name="resumes",
#         metadata={"hnsw:space": "cosine"}
#     )

# def store_embeddings(embedding, metadata: dict):
#     collection = get_collection()
#     collection.add(
#         embeddings=[embedding],
#         metadatas=[metadata],
#         ids=[metadata["id"]]
#     )
