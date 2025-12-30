import os
import google.generativeai as genai

# Check if API key is set
if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY environment variable not set.")
    exit(1)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception as e:
    print(f"Error initializing model: {e}")
    exit(1)

chat = model.start_chat(history=[])

print("Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == 'exit':
        print("Exiting the chat...")
        break

    try:
        response = chat.send_message(user_input)
        print(f"Bot: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}\n")
