import streamlit as st
import google.generativeai as genai

# Setup Gemini with Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load model
model = genai.GenerativeModel(model_name="models/gemini-pro")


# App UI
st.set_page_config(page_title="Mont & Paix Chatbot", page_icon="🏨")
st.title("🏨 Mont & Paix Front Desk Assistant")
st.markdown("Jullay! Ask anything about our rooms, facilities, or Pangong.")

# Store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display previous messages
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Ask something...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.history.append({"role": "user", "content": prompt})

    # Generate reply
    response = model.generate_content(prompt)
    reply = response.text

    st.chat_message("assistant").markdown(reply)
    st.session_state.history.append({"role": "assistant", "content": reply})

# Optional phone link
st.markdown("📞 [Call Front Desk](tel:+919876543210)", unsafe_allow_html=True)
