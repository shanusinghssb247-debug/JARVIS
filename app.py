import streamlit as st
from google import genai

# --- 1. Page Configuration & Styling ---
st.set_page_config(
    page_title="Free Gemini AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# --- 2. User Interface Headers ---
st.title("🤖 Free Gemini AI Assistant")
st.markdown("""
Welcome to your custom AI Web Application! 🚀  
This app is powered by Google's **Gemini 2.5 Flash** model and built entirely with Python.
""")
st.markdown("---")

# --- 3. Secure API Key Validation ---
# Streamlit looks for secrets in st.secrets when deployed or in a local secrets file.
if "GEMINI_API_KEY" not in st.secrets or not st.secrets["GEMINI_API_KEY"]:
    st.error("🔑 **API Key Missing:** We couldn't find your `GEMINI_API_KEY`.")
    st.info("""
    **How to fix this:**
    * **Locally:** Create a folder named `.streamlit` in your project directory, then add a file named `secrets.toml` inside it containing:  
      `GEMINI_API_KEY = "your_actual_api_key"`
    * **Streamlit Cloud:** Paste your key under **Advanced Settings -> Secrets** during or after deployment.
    """)
    st.stop()  # Safely halt app execution if the key is missing

# Safely extract the secret key
api_key = st.secrets["GEMINI_API_KEY"]

# --- 4. Initialize the Modern Google GenAI Client ---
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Failed to initialize the Gemini client: {e}")
    st.stop()

# --- 5. User Input Layout ---
user_prompt = st.text_area(
    label="What would you like to ask or generate?",
    placeholder="Type your question, code request, or writing prompt here...",
    height=150
)

# Create a clean row with a primary action button
if st.button("Generate Response", type="primary"):
    # Input validation
    if not user_prompt.strip():
        st.warning("⚠️ Please type something in the text area before clicking generate.")
    else:
        # Trigger an intuitive loading spinner while waiting for the API response
        with st.spinner("🧠 AI is thinking..."):
            try:
                # Call the new unified Google GenAI SDK
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_prompt
                )
                
                # --- 6. Success Output Handling ---
                st.success("✨ Response Generated Successfully:")
                st.markdown(response.text)
                
            except Exception as e:
                # --- 7. Comprehensive Error Handling ---
                st.error("❌ **An error occurred while communicating with the Gemini API.**")
                st.code(str(e), language="python")
                st.info("Tip: Double-check your API key validity and network connection.")
