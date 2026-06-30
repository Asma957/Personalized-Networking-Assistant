# Project Development Phase

## Overview
Complete source code for Personalized Networking Assistant.

## Project Structure
- backend/main.py — FastAPI server & routes
- backend/event_analyzer.py — Gemini AI theme extraction
- backend/topic_generator.py — Conversation starter generation
- backend/fact_checker.py — Wikipedia fact verification
- backend/tests/test_services.py — Unit tests
- data/history.json — Conversation history
- data/feedback.json — User feedback
- frontend.py — Streamlit UI
- main.py — App launcher
- requirements.txt — Dependencies

## Tech Stack Used
- Frontend: Streamlit
- Backend: FastAPI + Uvicorn
- AI Model: Google Gemini 2.0 Flash
- Fact Check: Wikipedia API
- Testing: Pytest
- Storage: Local JSON Files

## Key Features Implemented
1. AI-powered conversation starter generation
2. Event theme extraction using Gemini
3. Real-time Wikipedia fact verification
4. Conversation history with JSON persistence
5. User feedback system (thumbs up/down)
6. RESTful API with 5 endpoints

## How to Run
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Add API key in .env file
GEMINI_API_KEY=your_key_here

# Step 3: Run Backend
cd backend
python -m uvicorn main:app --reload --port 8000

# Step 4: Run Frontend
streamlit run frontend.py
