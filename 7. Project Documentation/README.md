# Project Documentation

## Project Overview
Personalized Networking Assistant is an AI-powered web application that generates smart, tailored conversation starters for professional networking events using Google Gemini AI and Wikipedia API.

## Tech Stack
| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI + Uvicorn |
| AI Model | Google Gemini 2.0 Flash |
| Fact Check | Wikipedia API |
| Testing | Pytest (15 tests passed) |
| Storage | Local JSON Files |

## API Documentation

### POST /generate-conversation
```json
Input: {"event_description": "AI Conference", "interests": "machine learning"}
Output: {"starters": ["...", "...", "..."], "event_analysis": {}, "entry_id": 1}
```

### POST /fact-check
```json
Input: {"query": "blockchain in healthcare"}
Output: {"result": {"found": true, "title": "...", "summary": "...", "source": "..."}}
```

### GET /history
```json
Output: {"history": [...], "total": 5}
```

## Challenges & Solutions
| Challenge | Solution |
|-----------|---------|
| API quota limits | Fallback starters implemented |
| History not saving | Fixed using absolute file path |
| Package compatibility | Used google-genai instead of google-generativeai |
| Disk space issue | Removed venv from git tracking |

## Project Outcomes
- ✅ AI-powered conversation starter generation
- ✅ Wikipedia fact verification
- ✅ Conversation history & feedback system
- ✅ 15 unit tests passed
- ✅ FastAPI REST API with 5 endpoints
- ✅ Streamlit interactive UI

## Future Enhancements
1. User authentication
2. PostgreSQL database
3. Mobile responsive UI
4. Multi-language support

## Developer
- Name: Janda Asma
- Project: Personalized Networking Assistant
- Track: AI/ML & Gen AI
