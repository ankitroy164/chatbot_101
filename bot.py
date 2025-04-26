import streamlit as st
import requests
import json

# --- Step 1: Set your API key and model (Move API Key to Streamlit Secrets) ---
# It's best practice to store API keys in Streamlit Secrets for security.
# Instructions on how to add secrets are below.
OPENROUTER_API_KEY = st.secrets["OPENROUTER_API_KEY"]
MODEL = "mistralai/mistral-tiny"  # Choose a free model (check OpenRouter's list)

# --- Step 2: Define the chatbot function ---
def chatbot(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error communicating with the API: {e}"
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        return f"Error processing the API response: {e}"

# --- Step 3: Streamlit UI ---
st.title("Simple Chatbot using OpenRouter")
st.markdown("Type your message and press Enter.")

# Initialize chat history in Streamlit Session State
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat messages from history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Your message"):
    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})
    # Display user message in the chat container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from the chatbot
    bot_response = chatbot(prompt)

    # Add bot response to chat history
    st.session_state["messages"].append({"role": "assistant", "content": bot_response})
    # Display bot response in the chat container
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# --- Instructions for adding API key to Streamlit Secrets ---
st.sidebar.header("Configuration")
st.sidebar.markdown("""
**To run this Streamlit app, you need to add your OpenRouter API key as a Streamlit secret.**

**Steps:**

1.  Go to your Streamlit Cloud dashboard ([https://streamlit.io/cloud](https://streamlit.io/cloud)).
2.  Select the app you want to deploy (or create a new one).
3.  Click on the **"Secrets"** button in the top right corner.
4.  In the "Secrets" section, add a new secret with the following key-value pair:

    ```
    OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"
    ```

    Replace `"YOUR_OPENROUTER_API_KEY"` with your actual OpenRouter API key.
5.  Streamlit will automatically load this secret when your app runs.

**Note:** Storing API keys directly in your code is insecure, especially when deploying applications. Streamlit Secrets provides a safe way to manage sensitive information.
""")