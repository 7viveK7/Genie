from openai import OpenAI
import json
from config import Config
from utils.json_utils import safe_json_loads


client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_summary(resume: str, job_description: str) -> dict:
    """Generate match summary using GPT"""
    prompt = f"""
    You are an AI career assistant. Analyze this resume against the job description:

    Resume:
    {resume}

    Job Description:
    {job_description}

    Respond in JSON format:
    {{
        "match_summary": "...",
        "career_suggestions": ["...", "..."]
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        
        return safe_json_loads(response.choices[0].message.content)
    except Exception as e:
        return {
            "match_summary": f"Error generating summary: {str(e)}",
            "career_suggestions": []
        }
