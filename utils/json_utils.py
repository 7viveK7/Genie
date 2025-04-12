import json
import re

def clean_json_response(text: str) -> str:
    """Remove markdown formatting like ```json ... ```"""
    cleaned = re.sub(r"```(?:json)?\n?(.*?)```", r"\1", text.strip(), flags=re.DOTALL)
    return cleaned.strip()

def safe_json_loads(text: str) -> dict:
    """Safely parse GPT output that might be wrapped in markdown or invalid format."""
    try:
        cleaned = clean_json_response(text)
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        print(f"[JSON Decode Error]: {str(e)}")
        print(f"[Raw GPT Output]: {text}")
        return {
            "match_summary": f"Error generating summary: {str(e)}",
            "career_suggestions": [],
            "flags": {"missing_skills": []},
            "interview_questions": [],
            "topics_to_cover": []
        }
