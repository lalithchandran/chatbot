import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Generation settings
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Start a persistent chat session
chat_session = model.start_chat()

# Welcome message
print("Welcome to the Chatbot!")
print("Bot: Hello! How can I assist you today?\n")

# Main chat loop
while True:
    try:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day!")
            break

        # Send message and get response
        response = chat_session.send_message(user_input)
        print(f"Bot: {response.text}\n")

    except Exception as e:
        print(f"Bot: Sorry, an error occurred: {e}\n")


# python d:\project\chatbot\chatbot\chat.py