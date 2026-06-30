import google.genai as genai

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_event(event_description: str) -> dict:
    try:
        prompt = f"""Analyze this networking event and extract themes.
Event: {event_description}

Respond in EXACTLY this format:
THEMES: theme1, theme2, theme3
INDUSTRY: industry name
TONE: professional"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        text = response.text.strip()
        themes, industry, tone = ["Networking", "Technology"], "General", "professional"
        
        for line in text.split("\n"):
            line = line.strip()
            if line.startswith("THEMES:"):
                themes = [t.strip() for t in line.replace("THEMES:", "").split(",")]
            elif line.startswith("INDUSTRY:"):
                industry = line.replace("INDUSTRY:", "").strip()
            elif line.startswith("TONE:"):
                tone = line.replace("TONE:", "").strip()
        
        return {"themes": themes, "industry": industry, "tone": tone}
    
    except Exception as e:
        return {"themes": ["Networking"], "industry": "General", "tone": "professional", "error": str(e)}