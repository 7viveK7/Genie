import streamlit as st
from utils import call_hiregenius_api
import base64

# ---------- App Config ----------
st.set_page_config(
    page_title="Genie - AI Hiring Assistant",
    page_icon="🧠",
    layout="centered"
)

# ---------- Hide Default Streamlit Header/Footer ----------
st.markdown("""
    <style>
        header.stAppHeader {display: none;}
        footer {visibility: hidden;}
        .stDecoration {display: none;}
        .stAppToolbar {display: none !important;}
        .stToolbarActions {display: none !important;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ---------- Custom Banner ----------
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color:#4CAF50;">Genie</h1>
        <h4>AI-Powered Resume Matcher & Career Advisor</h4>
        <p style="color:gray;">Upload your resume and match it against a job description. 
        Get a relevance score, feedback, interview questions, and growth tips instantly.</p>
    </div>
""", unsafe_allow_html=True)

# ---------- Input Form ----------
with st.form("resume_form"):
    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    job_description = st.text_area("📝 Paste Job Description", height=200)
    submitted = st.form_submit_button("🔍 Analyze Resume")

# ---------- Output Results ----------
if submitted:
    if uploaded_file and job_description:
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("🚧 Analyzing resume using AI..."):
            result = call_hiregenius_api("temp_resume.pdf", job_description)

        st.success("✅ Analysis Complete")

        st.markdown("### 📊 Relevance Score")
        st.progress(result["relevance_score"])
        st.markdown(f"**Score:** `{result['relevance_score'] * 100}`%")

        st.markdown("### ✨ Match Summary")
        st.info(result["match_summary"])

        st.markdown("### 🚀 Career Suggestions")
        for tip in result["career_suggestions"]:
            st.write(f"✅ {tip}")

        st.markdown("### 🎯 Topics to Learn")
        for topic in result["topics_to_cover"]:
            st.write(f"📘 {topic}")

        st.markdown("### 🧠 AI-Generated Interview Questions")
        for i, q in enumerate(result["interview_questions"], 1):
            st.write(f"**{i}. {q['question']}**")
            st.write(f"**Answer:** {q['answer']}")

    else:
        st.warning("⚠️ Please upload a PDF and enter a job description.")

# ---------- Custom Footer ----------
st.markdown("""
    <hr style="margin-top: 3rem;">
    <div style="text-align: center; font-size: 0.9rem; color: gray;">
        Made with ❤️ by <b>Vivekananda Malladi</b> • Powered by <a href="https://openai.com" target="_blank">OpenAI</a>
    </div>
""", unsafe_allow_html=True)
