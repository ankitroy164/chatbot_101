# 🛠️ Simple Chatbot using OpenRouter and Streamlit

This is a **self-project** where I built a simple chatbot web app using [Streamlit](https://streamlit.io/) and [OpenRouter](https://openrouter.ai/)'s API.  
The goal was to create a lightweight, interactive chat interface powered by an LLM (Large Language Model) — specifically, the **Mistral Tiny** model — while following best practices for handling API keys securely.

---

## ✨ Features
- Real-time conversation powered by OpenRouter's API.
- Persistent chat history using Streamlit's session state.
- User-friendly interface with Streamlit's latest chat elements.
- Secure handling of API keys via **Streamlit Secrets**.
- Minimalistic, clean, and beginner-friendly codebase.

---

## 🧠 How It Works
1. **API Connection**:  
   The app connects to the OpenRouter API using a secure API key stored in Streamlit Secrets.

2. **Sending Messages**:  
   When a user sends a message, it is forwarded as a prompt to the OpenRouter API along with the selected model.

3. **Receiving Responses**:  
   The app processes the API's response and displays the model's reply as part of an ongoing chat conversation.

4. **Session Management**:  
   Both user messages and bot replies are stored in the Streamlit session state, maintaining the full conversation even when the app reruns.

---

## 🚀 How to Run Locally

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/simple-chatbot-openrouter.git
   cd simple-chatbot-openrouter

3. **Set up Streamlit Secrets**:
   - Create a `.streamlit/secrets.toml` file inside your project directory.
   - Add your OpenRouter API key in the following format:
     ```toml
     [default]
     OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"
     ```

4. **Run the app**:
   ```bash
   streamlit run app.py


## 📚 Future Enhancements
- Allow model selection dynamically from the UI.
- Improve conversation memory (e.g., summarizing long histories).
- Retain all history as PDF

---

## 📬 Connect with Me

If you liked this project or have any suggestions, feel free to reach out!

- [LinkedIn](https://www.linkedin.com/in/yashkumarroy/)
- [GitHub](https://github.com/SpidY21)

---

**Made with ❤️ using Streamlit and OpenRouter**

