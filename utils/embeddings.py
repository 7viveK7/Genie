from langchain_openai import OpenAIEmbeddings
from config import Config

def get_embedder():
    return OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY,
                         )

def embed_text(text: str):
    """Generate embedding for given text"""
    embedder = get_embedder()
    return embedder.embed_query(text)
# import random

# def embed_text(text: str):
#     """Return a dummy embedding vector (for local testing)"""
#     random.seed(hash(text))  # Make sure same text gives same vector
#     return [random.uniform(-1, 1) for _ in range(1536)]
