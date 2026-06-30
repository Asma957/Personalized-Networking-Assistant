# Requirement Analysis

## Functional Requirements

### 1. Conversation Starter Generation
- User inputs event description and interests
- System extracts themes using Google Gemini AI
- System generates 3 personalized conversation starters
- User can provide thumbs up/down feedback

### 2. Fact Verification
- User inputs any topic/query
- System searches Wikipedia API
- Returns summary, source URL, and related topics

### 3. Conversation History
- System saves all generated conversations locally
- User can view past sessions with timestamps
- History stored in JSON format

## Non-Functional Requirements
- Response time under 10 seconds
- User-friendly Streamlit interface
- Modular and maintainable code structure
- RESTful API using FastAPI

## Technology Stack
| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Model | Google Gemini 1.5 Flash |
| Fact Check | Wikipedia API |
| Storage | Local JSON Files |
| Testing | Pytest |

## User Stories
1. As a user, I want to generate conversation starters for my networking event
2. As a user, I want to fact-check topics before attending events
3. As a user, I want to review my past conversation strategies
4. As a user, I want to provide feedback on generated starters
