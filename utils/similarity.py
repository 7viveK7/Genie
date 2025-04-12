import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


def cosine_similarity(vec1, vec2) -> float:
    """Calculate cosine similarity between two vectors"""
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))


def extract_missing_skills(resume_text: str, job_description: str) -> list:
    """Basic skill gap detection based on JD and resume content"""
    jd_words = set(map(str.lower, job_description.split()))
    resume_words = set(map(str.lower, resume_text.split()))

    gap = jd_words - resume_words
    filtered = [
        word for word in gap
        if word not in ENGLISH_STOP_WORDS and len(word) > 2 and word.isalpha()
    ]

    return list(filtered)[:10]

