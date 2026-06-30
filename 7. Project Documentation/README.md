# Project Documentation

## Project Overview
Personalized Networking Assistant is an AI-powered web application that generates smart, tailored conversation starters for professional networking events.

## Architecture
- **Frontend:** Streamlit (Port 8501)
- **Backend:** FastAPI (Port 8000)
- **AI:** Google Gemini 2.0 Flash
- **Fact Check:** Wikipedia API
- **Storage:** Local JSON Files

## API Documentation

### POST /generate-conversation
Input:
```json
{
  "event_description": "AI Conference 2026",
  "interests": "machine learning, NLP"
}
```
Output:
```json
{
  "starters": ["Starter 1", "Starter 2", "Starter 3"],
  "event_analysis": {"themes": [], "industry": "", "tone": ""},
  "entry_id": 1
}
```

### POST /fact-check
Input:
```json
{"query": "blockchain in healthcare"}
```
Output:
```json
{
  "result": {
    "found": true,
    "title": "Blockchain",
    "summary": "...",
    "source": "https://en.wikipedia.org/..."
  }
}
```

## Challenges & Solutions
| Challenge | Solution |
|-----------|---------|
| API quota limits | Fallback starters implemented |
| History not saving | Fixed file path using absolute path |
| Fact check wrong results | Improved Wikipedia search algorithm |

## Future Enhancements
1. User authentication system
2. Database integration (PostgreSQL)
3. Mobile responsive UI
4. Multi-language support
5. Email notifications

## Developer
- Name: Janda Asma
- Project: Personalized Networking Assistant
- Duration: 2 weeks
