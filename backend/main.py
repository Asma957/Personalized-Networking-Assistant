from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from event_analyzer import analyze_event
from topic_generator import generate_starters, save_feedback, get_history
from fact_checker import fact_check

app = FastAPI(
    title="Personalized Networking Assistant API",
    description="AI-powered conversation starter generator for networking events",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Request Models ----------
class GenerateRequest(BaseModel):
    event_description: str
    interests: str

class FeedbackRequest(BaseModel):
    entry_id: int
    starter_index: int
    feedback: str  # "thumbs_up" or "thumbs_down"

class FactCheckRequest(BaseModel):
    query: str

class AnalyzeRequest(BaseModel):
    event_description: str

# ---------- Routes ----------
@app.get("/")
def root():
    return {
        "message": "Personalized Networking Assistant API is running!",
        "version": "1.0.0",
        "endpoints": [
            "/generate-conversation",
            "/fact-check",
            "/analyze-event",
            "/history",
            "/feedback"
        ]
    }

@app.post("/generate-conversation")
def generate_conversation(request: GenerateRequest):
    try:
        # Step 1: Analyze event
        analysis = analyze_event(request.event_description)
        
        # Step 2: Generate starters
        result = generate_starters(
            event_description=request.event_description,
            interests=request.interests,
            themes=analysis["themes"]
        )
        
        return {
            "status": "success",
            "event_analysis": analysis,
            "starters": result["starters"],
            "entry_id": result["entry_id"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/fact-check")
def verify_fact(request: FactCheckRequest):
    try:
        result = fact_check(request.query)
        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-event")
def analyze(request: AnalyzeRequest):
    try:
        result = analyze_event(request.event_description)
        return {"status": "success", "analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
def history():
    try:
        data = get_history()
        return {"status": "success", "history": data, "total": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/feedback")
def feedback(request: FeedbackRequest):
    try:
        result = save_feedback(request.entry_id, request.starter_index, request.feedback)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))