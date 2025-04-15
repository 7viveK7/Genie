from langchain_openai import OpenAIEmbeddings
from app.config.settings import Config

def get_embedder():
    return OpenAIEmbeddings(openai_api_key=Config.OPENAI_API_KEY,
                         )

def embed_text(text: str):
    """Generate embedding for given text"""
    embedder = get_embedder()
    return embedder.embed_query(text)
