import streamlit as st
from google import genai
from google.genai import errors

# --- PAGE SETUP ---
st.set_page_config(page_title="Gemini 2.5 Flash App", page_icon="⚡")
st.title("⚡ My Gemini 2.5 Flash App")

# --- AUTHENTICATION & CLIENT SETUP ---
# Fetch the API key from Streamlit secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("Error: 'GEMINI_API_KEY' not found in Streamlit secrets. Please check your .streamlit/secrets.toml file.")
    st.stop()

# Initialize the NEW SDK client
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize the Gemini client: {e}")
    st.stop()

# --- USER INTERFACE ---
st.write("Type a prompt below to generate a response using the free-tier optimized `gemini-2.5-flash` model.")

user_prompt = st.text_area("Enter your prompt:", placeholder="What can you do for me today?")

if st.button("Generate Response"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt before generating.")
    else:
        with st.spinner("Generating response..."):
            try:
                # --- API CALL USING NEW SYNTAX ---
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_prompt
                )
                
                # Display the result
                st.success("Success!")
                st.write(response.text)

            except errors.APIError as api_err:
                # Catching specific API errors like 401, 404, or 429
                st.error(f"API Error: {api_err.message} (Code: {api_err.code})")
            except Exception as e:
                # Catching any other unexpected errors
                st.error(f"An unexpected error occurred: {e}")
