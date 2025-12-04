# streamlit_app.py
import streamlit as st
import requests

BACKEND_URL = "https://ai-assistant-backend-1-0wwp.onrender.com"

st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

st.title("🤖 AI Assistant")
st.caption("Powered by FastAPI + OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "session_id" not in st.session_state:
    st.session_state.session_id = "user123"

MODES = ["General Assistant", "Code Assistant", "Study Helper", "Career Guide"]
mode = st.sidebar.selectbox("Assistant Mode", MODES)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    headers = {
        "x-api-key": "dev-key",
        "Content-Type": "application/json"
    }

    payload = {
        "session_id": st.session_state.session_id,
        "mode": mode,
        "messages": st.session_state.messages
    }

    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json=payload,
            headers=headers,
            timeout=60
        )

        if response.status_code != 200:
            st.error(f"Backend error {response.status_code}: {response.text}")
            st.stop()

        data = response.json()
        reply = data.get("reply", "No reply returned")

        st.session_state.session_id = data.get("session_id", st.session_state.session_id)

        st.session_state.messages.append({"role": "assistant", "content": reply})

        with st.chat_message("assistant"):
            st.markdown(reply)

    except Exception as e:
        st.error(f"Request failed: {e}")
