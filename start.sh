#!/bin/bash

echo " Installing Dependencies..."
pip install -r requirements.txt

echo "Starting FastAPI Server..."
uvicorn app.main:app --reload
