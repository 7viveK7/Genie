from pydantic import BaseModel

class MatchResponse(BaseModel):
    filename: str
    relevance_score: float
    match_summary: str
    career_suggestions: list[str]