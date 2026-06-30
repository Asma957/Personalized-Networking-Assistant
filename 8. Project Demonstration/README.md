# Project Demonstration

## Demo Video
[To be added after recording]

## Application Screenshots

### Main Interface
- 3 tabs: Generate Starters, Fact Check, History
- Clean and interactive UI

### Tab 1: Generate Conversation Starters
- Enter event description
- Enter your interests
- Click Generate button
- Get 3 AI-powered starters
- Give thumbs up/down feedback

### Tab 2: Fact Check
- Enter any topic
- Get Wikipedia summary
- View source URL
- See related topics

### Tab 3: Conversation History
- Click Load History
- View all past sessions
- See timestamps and starters

## How to Run

### Prerequisites
- Python 3.10+
- Google Gemini API Key (from aistudio.google.com)

### Steps
1. Clone repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Create `.env` file: `GEMINI_API_KEY=your_key`
6. Run backend: `cd backend && python -m uvicorn main:app --reload --port 8000`
7. Run frontend: `streamlit run frontend.py`
8. Open: `http://localhost:8501`

## Test Results
- Total Tests: 15
- Passed: 15 ✅
- Failed: 0

## GitHub Repository
https://github.com/Asma957/Personalized-Networking-Assistant
