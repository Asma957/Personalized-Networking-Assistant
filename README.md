<<<<<<< HEAD
# 🤝 Personalized Networking Assistant

An AI-powered web application that generates smart, tailored conversation starters for professional and social networking events.

## 🚀 Features

- **Smart Conversation Starters** — AI-generated, context-aware prompts using Google Gemini
- **Event Theme Analysis** — Extracts key themes from event descriptions
- **Fact Verification** — Real-time fact checking using Wikipedia API
- **Conversation History** — Saves and reviews past generated starters
- **Feedback System** — Thumbs up/down to improve personalization

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Model | Google Gemini 1.5 Flash |
| NLP | DistilBERT (Zero-Shot Classification) |
| Fact Check | Wikipedia API |
| Testing | Pytest |
| Storage | Local JSON Files |

## 📁 Project Structure
Personalized-Networking-Assistant/

├── backend/

│   ├── main.py               # FastAPI server

│   ├── event_analyzer.py     # Theme extraction

│   ├── topic_generator.py    # Conversation generator

│   ├── fact_checker.py       # Wikipedia fact check

│   └── tests/

│       └── test_services.py  # Unit tests

├── data/

│   ├── history.json          # Conversation history

│   └── feedback.json         # User feedback

├── frontend.py               # Streamlit UI

├── main.py                   # App launcher

├── requirements.txt          # Dependencies

├── .env                      # API Keys (not committed)

├── .gitignore                # Git ignore file

└── README.md                 # Documentation

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Personalized-Networking-Assistant.git
cd Personalized-Networking-Assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file:
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"

### 5. Run the Application
Terminal 1 - Backend:
```bash
cd backend
uvicorn main:app --reload --port 8000
```
Terminal 2 - Frontend:
```bash
streamlit run frontend.py
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API health check |
| POST | `/generate-conversation` | Generate starters |
| POST | `/fact-check` | Verify facts |
| POST | `/analyze-event` | Analyze themes |
| GET | `/history` | Get history |
| POST | `/feedback` | Save feedback |

## 🧪 Running Tests
```bash
cd backend
pytest tests/ -v
```

## 👥 Team Members
- [Janda Asma] — Developer

## 📄 License
MIT License
=======
# Personalized-Networking-Assistant
>>>>>>> cf4ac85ec16080d8f72bad7d8e687b08349dfd02
