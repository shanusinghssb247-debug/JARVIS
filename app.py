import streamlit as st
from google import genai
from google.genai import errors

st.title("⚡ My Gemini 2.5 Flash App")

# API key pull karo
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("Error: Key not found in secrets.")
    st.stop()

# Simple Client initialize karo (No Vertex)
client = genai.Client(api_key=api_key)

user_prompt = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    if user_prompt:
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt
            )
            st.success("Success!")
            st.write(response.text)
        except errors.APIError as api_err:
            st.error(f"API Error: {api_err.message}")
