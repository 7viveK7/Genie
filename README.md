# 🚀 HIREGENIUS - AI-Powered Hiring Assistant

HIREGENIUS is a next-gen AI-powered virtual hiring consultant that transforms the hiring workflow by automating resume parsing, skill matching, candidate scoring, and career feedback generation using cutting-edge LLMs and vector databases.

## 🔍 Core Features
- Upload resume (PDF) + job description
- AI calculates **Relevance Score** using embeddings
- GPT generates **Match Summary**
- GPT provides **Career Suggestions**
- Modular FastAPI backend, embeddable in any HR workflow

## 📦 Tech Stack
- FastAPI, Python, LangChain, OpenAI, ChromaDB, pdfplumber
- Streamlit (UI, coming Day 4)
- Docker-ready, scalable, cloud-deployable

## 🏁 Quick Start

```bash
git clone https://github.com/7viveK7/Genie.git
cd Genie
cp .env.example .env  # Add your OpenAI key inside .env
pip install -r requirements.txt
bash run.sh
