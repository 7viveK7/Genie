from pydantic import BaseModel
from typing import List, Dict

class InterviewQuestion(BaseModel):
    question: str
    answer: str

class Flags(BaseModel):
    missing_skills: List[str]

class MatchResponse(BaseModel):
    filename: str
    relevance_score: float
    match_summary: str
    career_suggestions: List[str]
    interview_questions: List[Dict[str, str]]
    topics_to_cover: List[str]
    flags: Flags