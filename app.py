import streamlit as st
import google.generativeai as genai

# Page styling
st.set_page_config(page_title="Shanu's AI Tool", page_icon="🚀", layout="centered")

# Title and header
st.title("🚀 POWERFUL AI MADE BY SHANU")
st.write("Welcome! Powered by Gemini Pro for heavy-duty brainpower.")

# Fetch your secret API key safely
api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ API Key is missing! Please double-check your Streamlit Secrets setting.")
else:
    # Initialize Google Gemini
    genai.configure(api_key=api_key)
    
    # User Input
    user_prompt = st.text_input("Ask me anything:", placeholder="Type your prompt here...")
    
    # Action Button
    if st.button("Generate Answer ✨"):
        if user_prompt:
            with st.spinner("Gemini Pro is processing..."):
                try:
                    # Updated to the official stable free-tier Pro model
                    model = genai.GenerativeModel("gemini-2.5-pro")
                    response = model.generate_content(user_prompt)
                    
                    st.success("Here is what I found:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
        else:
            st.warning("Please type a question or prompt first!")
