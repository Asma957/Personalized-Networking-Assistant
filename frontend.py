import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Personalized Networking Assistant", page_icon="🤝", layout="wide")

st.markdown("""
<style>
.main-header{font-size:2.5rem;font-weight:bold;color:#1E3A5F;text-align:center;padding:1rem;}
.starter-card{background-color:#f0f7ff;border-left:4px solid #1E90FF;padding:1rem;border-radius:8px;margin:0.5rem 0;}
.fact-card{background-color:#f0fff4;border-left:4px solid #28a745;padding:1rem;border-radius:8px;margin:0.5rem 0;}
.history-card{background-color:#fff8f0;border-left:4px solid #fd7e14;padding:1rem;border-radius:8px;margin:0.5rem 0;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🤝 Personalized Networking Assistant</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Generate smart, AI-powered conversation starters!</p>", unsafe_allow_html=True)
st.divider()

tab1, tab2, tab3 = st.tabs(["💬 Generate Starters", "🔍 Fact Check", "📜 History"])

with tab1:
    st.subheader("🎯 Generate Conversation Starters")
    col1, col2 = st.columns(2)
    with col1:
        event_desc = st.text_area("📋 Event Description", placeholder="e.g., AI for Sustainable Cities", height=150)
    with col2:
        user_interests = st.text_input("💡 Your Interests", placeholder="e.g., climate change, urban planning")
        st.info("💡 **Tip:** Be specific about your interests!")

    if st.button("🚀 Generate Conversation Starters", use_container_width=True):
        if event_desc and user_interests:
            with st.spinner("🤖 AI is generating starters..."):
                try:
                    response = requests.post(
                        f"{API_URL}/generate-conversation",
                        json={"event_description": event_desc, "interests": user_interests},
                        timeout=30
                    )
                    if response.status_code == 200:
                        data = response.json()
                        starters = data.get("starters", [])
                        entry_id = data.get("entry_id", 1)
                        analysis = data.get("event_analysis", {})

                        st.success("✅ Here are your conversation starters!")

                        if analysis:
                            with st.expander("🔎 Event Analysis"):
                                st.write(f"**Themes:** {', '.join(analysis.get('themes', []))}")
                                st.write(f"**Industry:** {analysis.get('industry', '')}")
                                st.write(f"**Tone:** {analysis.get('tone', '')}")

                        for i, starter in enumerate(starters, 1):
                            st.markdown(f'<div class="starter-card"><b>Starter {i}:</b><br>{starter}</div>', unsafe_allow_html=True)
                            c1, c2 = st.columns(2)
                            with c1:
                                if st.button(f"👍 Helpful", key=f"up_{i}"):
                                    requests.post(f"{API_URL}/feedback", json={"entry_id": entry_id, "starter_index": i, "feedback": "thumbs_up"})
                                    st.success("Thanks!")
                            with c2:
                                if st.button(f"👎 Not Helpful", key=f"down_{i}"):
                                    requests.post(f"{API_URL}/feedback", json={"entry_id": entry_id, "starter_index": i, "feedback": "thumbs_down"})
                                    st.warning("We'll improve!")
                    else:
                        st.error(f"❌ Backend error: {response.status_code} — {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend! Make sure FastAPI is running on port 8000.")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please fill in both fields!")

with tab2:
    st.subheader("🔍 Quick Fact Verification")
    query = st.text_input("🔎 Enter topic", placeholder="e.g., blockchain in healthcare")
    if st.button("🔍 Verify Fact", use_container_width=True):
        if query:
            with st.spinner("Searching Wikipedia..."):
                try:
                    response = requests.post(
                        f"{API_URL}/fact-check",
                        json={"query": query},
                        timeout=30
                    )
                    if response.status_code == 200:
                        text = response.text
                        if not text or text.strip() == "":
                            st.error("Empty response from backend!")
                        else:
                            data = response.json()
                            result = data.get("result", {})
                            if result.get("found"):
                                st.success(f"✅ Found: **{result['title']}**")
                                st.markdown(f'<div class="fact-card"><b>📖 Summary:</b><br>{result["summary"]}</div>', unsafe_allow_html=True)
                                if result.get("source"):
                                    st.markdown(f"🔗 [Read more]({result['source']})")
                                if result.get("related_topics"):
                                    st.write("**📚 Related Topics:**")
                                    for topic in result["related_topics"]:
                                        st.write(f"• {topic}")
                            else:
                                st.warning(result.get("summary", "Not found"))
                    else:
                        st.error(f"Backend error: {response.status_code}")
                except requests.exceptions.Timeout:
                    st.error("❌ Request timed out! Try again.")
                except requests.exceptions.ConnectionError:
                    st.error("❌ Cannot connect to backend!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("Please enter a topic!")

with tab3:
    st.subheader("📜 Conversation History")
    if st.button("🔄 Load History", use_container_width=True):
        try:
            response = requests.get(f"{API_URL}/history", timeout=10)
            if response.status_code == 200:
                data = response.json()
                history = data.get("history", [])
                if not history:
                    st.info("No history yet!")
                else:
                    st.success(f"Found {len(history)} session(s)!")
                    for entry in reversed(history):
                        with st.expander(f"🕐 {entry.get('timestamp','')}: {str(entry.get('event_description',''))[:50]}..."):
                            st.write(f"**Event:** {entry.get('event_description','')}")
                            st.write(f"**Interests:** {entry.get('interests','')}")
                            for i, s in enumerate(entry.get('starters', []), 1):
                                st.markdown(f'<div class="history-card"><b>Starter {i}:</b> {s}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")