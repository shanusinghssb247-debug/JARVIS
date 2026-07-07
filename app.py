import streamlit as st
from google import genai

# Page styling
st.set_page_config(page_title="Shanu's AI Tool", page_icon="🚀", layout="centered")

# Title and header
st.title("🚀 POWERFUL AI MADE BY SHANU")
st.write("Welcome! Powered by the latest Gemini SDK.")

# Fetch your secret API key safely
api_key = st.secrets.get("GEMINI_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ API Key is missing! Please double-check your Streamlit Secrets setting.")
else:
    try:
        # Initialize the modern Google GenAI Client designed for AQ. keys
        client = genai.Client(api_key=api_key)
        
        # User Input
        user_prompt = st.text_input("Ask me anything:", placeholder="Type your prompt here...")
        
        # Action Button
        if st.button("Generate Answer ✨"):
            if user_prompt:
                with st.spinner("Thinking..."):
                    # Using gemini-2.5-flash for maximum free quota compliance
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=user_prompt
                    )
                    
                    st.success("Here is what I found:")
                    st.write(response.text)
            else:
                st.warning("Please type a question or prompt first!")
                
    except Exception as e:
        st.error(f"Something went wrong during setup: {e}")
