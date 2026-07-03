import google.genai as genai
import json
import os
from datetime import datetime

GEMINI_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
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
        prompt = f"""You are an expert professional networking coach helping someone prepare for a networking event.

EVENT: {event_description}
PERSON'S INTERESTS: {interests}
KEY THEMES: {', '.join(themes) if themes else 'General Networking'}

Generate exactly 3 conversation starters. Each starter MUST be 3-4 sentences long. Structure each starter like this:
- Sentence 1: Open with a specific observation or hook about the event/theme
- Sentence 2: Connect it to a relevant insight or trend
- Sentence 3-4: End with an open-ended question that invites the other person to share

IMPORTANT: Each starter must be on its own line starting with STARTER1:, STARTER2:, STARTER3:
Do NOT split a starter across multiple lines.

Example format:
STARTER1: I've been following how [topic] is reshaping [industry] — it's fascinating to see it play out in real time. One thing I keep wondering about is [specific angle]. How are you seeing this impact your work, and do you think [follow-up question]?
STARTER2: [full 3-4 sentence starter on one line]
STARTER3: [full 3-4 sentence starter on one line]

Now generate for the event above:"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        if not response or not response.text:
            raise ValueError("Empty response from Gemini")
            
        text = response.text.strip()
        print(f"RAW GEMINI RESPONSE:\n{text}\n")

        # Parse response
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("STARTER1:"):
                starters.append(line.replace("STARTER1:", "").strip())
            elif line.startswith("STARTER2:"):
                starters.append(line.replace("STARTER2:", "").strip())
            elif line.startswith("STARTER3:"):
                starters.append(line.replace("STARTER3:", "").strip())

        print(f"Parsed {len(starters)} starters")

        # If parsing failed, try alternative parsing
        if len(starters) < 3:
            print("Trying alternative parsing...")
            starters = []
            current = ""
            for line in lines:
                line = line.strip()
                if line.startswith("STARTER"):
                    if current:
                        starters.append(current.strip())
                    current = line.split(":", 1)[1].strip() if ":" in line else ""
                elif current and line:
                    current += " " + line
            if current:
                starters.append(current.strip())
            print(f"Alternative parsing got {len(starters)} starters")

    except Exception as e:
        error_msg = str(e)
        print(f"GEMINI ERROR: {error_msg}")

    # Use rich fallback starters if still not enough
    if len(starters) < 3:
        theme = themes[0] if themes else "this field"
        interest_list = [i.strip() for i in interests.split(",")] if interests else ["this area"]
        i1 = interest_list[0] if len(interest_list) > 0 else "this area"
        i2 = interest_list[1] if len(interest_list) > 1 else i1

        starters = [
            f"I've been following developments in {theme} closely, and this event feels like exactly the right place to have deeper conversations about where things are heading. There's so much happening at the intersection of {i1} and {i2} that it's hard to keep up. What's your take on the biggest shift you've seen in this space recently — and do you think the industry is moving fast enough to adapt?",
            f"What originally drew me to this event was the focus on {theme} — it's one of those areas where the gap between what's possible and what's actually being implemented still feels huge. I've been particularly curious about how professionals with backgrounds in {i1} are navigating that gap in practice. Have you found that your own experience here has changed how you think about the broader challenges in {theme}?",
            f"Events like this are rare because they bring together people who are thinking seriously about {theme} from very different angles. I'm personally interested in {i2} and how it connects to some of the larger trends here. I'd love to hear what you're working on — what aspect of today's sessions are you most looking forward to, and what would make this event a success for you?"
        ]
        print("Using rich fallback starters")

    # Save to history
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