import google.genai as genai
import json
import os
from datetime import datetime

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
client = genai.Client(api_key=GEMINI_API_KEY)

HISTORY_FILE = r"C:\Users\janda\Personalized-Networking-Assistant\data\history.json"
FEEDBACK_FILE = r"C:\Users\janda\Personalized-Networking-Assistant\data\feedback.json"

def load_json(filepath):
    try:
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)
            return []
        with open(filepath, "r") as f:
            content = f.read().strip()
        if not content:
            return []
        return json.loads(content)
    except:
        return []

def save_json(filepath, data):
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Save error: {e}")
        return False

def generate_starters(event_description: str, interests: str, themes: list) -> dict:
    starters = []
    error_msg = None
    
    try:
        prompt = f"""You are an expert networking coach. Generate exactly 3 conversation starters.

Event: {event_description}
User Interests: {interests}
Themes: {', '.join(themes)}

Rules:
- Each starter must be unique and engaging
- Natural and conversational tone
- 1-2 sentences max each

Respond in EXACTLY this format:
STARTER1: [your starter here]
STARTER2: [your starter here]
STARTER3: [your starter here]"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        text = response.text.strip()
        
        for line in text.split("\n"):
            line = line.strip()
            if line.startswith("STARTER1:"):
                starters.append(line.replace("STARTER1:", "").strip())
            elif line.startswith("STARTER2:"):
                starters.append(line.replace("STARTER2:", "").strip())
            elif line.startswith("STARTER3:"):
                starters.append(line.replace("STARTER3:", "").strip())

    except Exception as e:
        error_msg = str(e)
        starters = [
            f"What aspect of {themes[0] if themes else 'this event'} interests you most?",
            f"How long have you been working in {interests.split(',')[0] if interests else 'this field'}?",
            f"What are you hoping to gain from this event?"
        ]

    if len(starters) < 3:
        starters = [
            f"What aspect of {themes[0] if themes else 'this event'} interests you most?",
            f"How long have you been working in this field?",
            f"What are you hoping to gain from this event?"
        ]

    # Always save to history
    history = load_json(HISTORY_FILE)
    entry = {
        "id": len(history) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_description": event_description,
        "interests": interests,
        "themes": themes,
        "starters": starters
    }
    history.append(entry)
    saved = save_json(HISTORY_FILE, history)
    print(f"History saved: {saved}, Total entries: {len(history)}")
    
    result = {"starters": starters, "entry_id": entry["id"]}
    if error_msg:
        result["error"] = error_msg
    return result

def save_feedback(entry_id: int, starter_index: int, feedback: str) -> dict:
    try:
        feedbacks = load_json(FEEDBACK_FILE)
        feedbacks.append({
            "entry_id": entry_id,
            "starter_index": starter_index,
            "feedback": feedback,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        save_json(FEEDBACK_FILE, feedbacks)
        return {"status": "success", "message": "Feedback saved!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_history() -> list:
    return load_json(HISTORY_FILE)