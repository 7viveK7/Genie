from openai import OpenAI
from app.config.settings import Config
from app.utils.json_utils import safe_json_loads

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_summary( 
    resume: str,
    job_description: str,
    relevance_score: float,
    missing_skills: list,
    filename: str
) -> dict:
    """Generate full summary with GPT including questions and suggestions"""
    prompt = f"""
You are an AI career assistant. Analyze the resume and job description. Respond in RAW JSON format (no markdown).

Expected format:
{{
  "match_summary": "Summary here...",
  "career_suggestions": ["Skill 1", "Skill 2"],
  "flags": {{
    "missing_skills": ["SkillA", "SkillB"]
  }},
  "interview_questions": [
    {{"question": "What is React?", "answer": "React is ..."}},
    ...
  ],
  "topics_to_cover": ["Topic 1", "Topic 2"]
}}

Resume:
{resume}

Job Description:
{job_description}

Generate questions that are hard, relevant to the experience level, and realistic.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        content = response.choices[0].message.content
        parsed = safe_json_loads(content)

        return {
            "filename": filename,
            "relevance_score": round(relevance_score, 2),
            **parsed,
            "flags": {
                "missing_skills": missing_skills
            }
        }

    except Exception as e:
        return {
            "filename": filename,
            "relevance_score": relevance_score,
            "match_summary": f"Error generating summary: {str(e)}",
            "career_suggestions": [],
            "flags": {"missing_skills": missing_skills},
            "interview_questions": [],
            "topics_to_cover": []
        }
