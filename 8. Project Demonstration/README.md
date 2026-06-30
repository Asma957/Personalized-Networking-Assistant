# Project Demonstration

## Demo Video
[Demo video link will be added after recording]

## Application Screenshots

### Tab 1: Generate Conversation Starters
- User enters event description and interests
- AI generates 3 personalized conversation starters
- User can provide thumbs up/down feedback

### Tab 2: Fact Check
- User enters any topic
- Wikipedia API returns summary and source
- Related topics also displayed

### Tab 3: Conversation History
- All past sessions displayed
- Timestamps and starters visible
- Expandable session cards

## How to Run the Application

### Prerequisites
- Python 3.10+
- Google Gemini API Key

### Steps
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Add API key in `.env` file
4. Run backend: `cd backend && python -m uvicorn main:app --reload --port 8000`
5. Run frontend: `streamlit run frontend.py`
6. Open browser: `http://localhost:8501`

## Live Demo
- Backend API: `http://127.0.0.1:8000`
- Frontend App: `http://localhost:8501`
- API Docs: `http://127.0.0.1:8000/docs`

## Key Features Demonstrated
1. ✅ AI conversation starter generation
2. ✅ Event theme analysis
3. ✅ Wikipedia fact verification
4. ✅ Conversation history
5. ✅ User feedback system
