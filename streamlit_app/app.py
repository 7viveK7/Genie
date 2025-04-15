import streamlit as st
from utils import call_hiregenius_api

st.set_page_config(page_title="HIREGENIUS", layout="centered")
st.title("🧠 HIREGENIUS AI Hiring Assistant")

with st.form("resume_form"):
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste Job Description")
    submitted = st.form_submit_button("Analyze")

if submitted:
    if uploaded_file and job_description:
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("Analyzing resume..."):
            result = call_hiregenius_api("temp_resume.pdf", job_description)

        st.subheader("✅ Match Summary")
        st.markdown(result["match_summary"])

        st.subheader("📊 Relevance Score")
        st.progress(result["relevance_score"])
        st.code(f"{result['relevance_score']}")

        st.subheader("🚀 Career Suggestions")
        for suggestion in result["career_suggestions"]:
            st.write(f"• {suggestion}")

        st.subheader("💡 Topics to Cover")
        for topic in result["topics_to_cover"]:
            st.write(f"📘 {topic}")

        st.subheader("🎤 AI Interview Questions")
        for i, q in enumerate(result["interview_questions"], 1):
            st.write(f"{i}. {q}")
    else:
        st.warning("Please upload a resume and provide a job description.")
