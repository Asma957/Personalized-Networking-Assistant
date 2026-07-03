import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Personalized Networking Assistant", page_icon="🤝", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: linear-gradient(135deg, #f8fbff, #eef4ff, #ffffff); }
#MainMenu, footer, header {visibility: hidden;}
.main-header { font-size: 2.4rem; font-weight: 700; background: linear-gradient(90deg, #4F8DFD, #7B61FF); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; padding: 1rem 0 0.2rem 0; }
.sub-header { text-align: center; color: #64748b; margin-bottom: 1.5rem; }
.card { background: #FFFFFF; border-radius: 25px; padding: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.06); margin-bottom: 1rem; }
.starter-card { background: #FFFFFF; border-left: 5px solid #4F8DFD; border-radius: 20px; padding: 20px 24px; margin: 0.7rem 0; box-shadow: 0 8px 30px rgba(0,0,0,0.05); }
.starter-num { display:inline-block; background: linear-gradient(135deg, #4F8DFD, #7B61FF); color: white; font-weight:700; border-radius: 50%; width: 32px; height: 32px; text-align:center; line-height:32px; margin-right: 10px; }
.starter-text { font-size: 1.05rem; color: #1E293B; line-height: 1.7; }
.fact-card { background: #FFFFFF; border-left: 5px solid #4FD1C5; border-radius: 20px; padding: 20px 24px; box-shadow: 0 8px 30px rgba(0,0,0,0.05); }
.history-card { background: #FFFFFF; border-left: 5px solid #7B61FF; border-radius: 20px; padding: 18px 22px; margin: 0.6rem 0; box-shadow: 0 6px 25px rgba(0,0,0,0.05); }
.stat-card { background: #FFFFFF; border-radius: 22px; padding: 18px 20px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); text-align: center; }
.stat-num { font-size: 1.8rem; font-weight: 700; color: #4F8DFD; }
.stat-label { color: #64748b; font-size: 0.85rem; }
.stButton>button { border-radius: 20px; background: linear-gradient(90deg, #4F8DFD, #7B61FF); color: white; border: none; padding: 0.6rem 1.2rem; font-weight: 600; }
.stTextInput>div>div>input, .stTextArea textarea { border-radius: 16px !important; border: 1px solid #E2E8F0 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🤝 Personalized Networking Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Generate smart, AI-powered conversation starters for your next networking event!</div>', unsafe_allow_html=True)

if "stats" not in st.session_state:
    st.session_state.stats = {"sessions": 0, "fact_checks": 0, "positive": 0}

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="stat-card"><div class="stat-num">{st.session_state.stats["sessions"]}</div><div class="stat-label">💬 Generated Sessions</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="stat-card"><div class="stat-num">{st.session_state.stats["fact_checks"]}</div><div class="stat-label">🔍 Fact Checks</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="stat-card"><div class="stat-num">{st.session_state.stats["positive"]}</div><div class="stat-label">👍 Positive Feedback</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-card"><div class="stat-num">92%</div><div class="stat-label">⚡ AI Accuracy</div></div>', unsafe_allow_html=True)

st.write("")
tab1, tab2, tab3 = st.tabs(["💬 Generate Starters", "🔍 Fact Check", "📜 History"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        event_desc = st.text_area("📋 Event Description", placeholder="e.g., AI for Sustainable Cities — a conference bringing together urban planners and AI researchers", height=140)
    with col2:
        user_interests = st.text_input("💡 Your Interests", placeholder="e.g., climate change, urban planning, machine learning")
        st.info("💡 Be specific about your interests for richer starters!")
    generate_clicked = st.button("🚀 Generate Conversation Starters", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if generate_clicked:
        if event_desc and user_interests:
            with st.spinner("🤖 AI is crafting personalized starters for you..."):
                try:
                    response = requests.post(
                        f"{API_URL}/generate-conversation",
                        json={"event_description": event_desc, "interests": user_interests},
                        timeout=60
                    )
                    if response.status_code == 200 and response.text.strip():
                        data = response.json()
                        starters = data.get("starters", [])
                        entry_id = data.get("entry_id", 1)
                        analysis = data.get("event_analysis", {})
                        st.session_state.stats["sessions"] += 1

                        st.success("✅ Here are your personalized conversation starters!")

                        if analysis:
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            ac1, ac2, ac3 = st.columns(3)
                            with ac1:
                                st.markdown(f"**🎯 Themes:** {', '.join(analysis.get('themes', []))}")
                            with ac2:
                                st.markdown(f"**🏭 Industry:** {analysis.get('industry', '')}")
                            with ac3:
                                st.markdown(f"**🎙️ Tone:** {analysis.get('tone', '')}")
                            st.markdown('</div>', unsafe_allow_html=True)

                        for i, starter in enumerate(starters, 1):
                            st.markdown(f"""
                            <div class="starter-card">
                                <span class="starter-num">{i}</span>
                                <span class="starter-text">{starter}</span>
                            </div>
                            """, unsafe_allow_html=True)
                            cu, cd = st.columns(2)
                            with cu:
                                if st.button("👍 Helpful", key=f"up_{i}_{entry_id}"):
                                    requests.post(f"{API_URL}/feedback", json={"entry_id": entry_id, "starter_index": i, "feedback": "thumbs_up"})
                                    st.session_state.stats["positive"] += 1
                                    st.success("Thanks!")
                            with cd:
                                if st.button("👎 Not Helpful", key=f"down_{i}_{entry_id}"):
                                    requests.post(f"{API_URL}/feedback", json={"entry_id": entry_id, "starter_index": i, "feedback": "thumbs_down"})
                                    st.warning("We'll improve!")
                    else:
                        st.error(f"Backend error: {response.status_code}")
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. Please try again.")
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend! Make sure FastAPI is running on port 8000.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please fill in both fields!")

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    query = st.text_input("🔎 Enter topic to fact-check", placeholder="e.g., blockchain in healthcare")
    verify_clicked = st.button("🔍 Verify Fact", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if verify_clicked:
        if query:
            with st.spinner("🔍 Searching Wikipedia..."):
                try:
                    response = requests.post(
                        f"{API_URL}/fact-check",
                        json={"query": query},
                        timeout=60
                    )
                    if response.status_code == 200 and response.text.strip():
                        data = response.json()
                        result = data.get("result", {})
                        st.session_state.stats["fact_checks"] += 1
                        if result.get("found"):
                            st.success(f"✅ Found: **{result['title']}**")
                            st.markdown(f'<div class="fact-card"><b>📖 Summary:</b><br><br>{result["summary"]}</div>', unsafe_allow_html=True)
                            if result.get("source"):
                                st.markdown(f"🔗 [Read more on Wikipedia]({result['source']})")
                            if result.get("related_topics"):
                                st.write("**📚 Related Topics:**")
                                for topic in result["related_topics"]:
                                    st.write(f"• {topic}")
                        else:
                            st.warning(result.get("summary", "Not found"))
                    else:
                        st.error("No response from backend. Please try again.")
                except requests.exceptions.Timeout:
                    st.error("⏱️ Request timed out. Please try again.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a topic!")

with tab3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    load_clicked = st.button("🔄 Load History", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    if load_clicked:
        try:
            response = requests.get(f"{API_URL}/history", timeout=30)
            if response.status_code == 200:
                data = response.json()
                history = data.get("history", [])
                if not history:
                    st.info("📭 No history yet!")
                else:
                    st.success(f"📚 Found {len(history)} session(s)!")
                    for entry in reversed(history):
                        with st.expander(f"🕐 {entry.get('timestamp','')} — {str(entry.get('event_description',''))[:50]}..."):
                            st.markdown(f"**Event:** {entry.get('event_description','')}")
                            st.markdown(f"**Interests:** {entry.get('interests','')}")
                            st.markdown(f"**Themes:** {', '.join(entry.get('themes',[]))}")
                            for i, s in enumerate(entry.get('starters', []), 1):
                                st.markdown(f'<div class="history-card"><b>Starter {i}:</b> {s}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")