import random

responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine!", "Doing great!", "I'm okay, thanks!"],
    "what is your name": ["I'm a Python chatbot.", "You can call me PyBot."],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

def preprocess_input(user_input) :
    return user_input.lower().strip()

def get_response(user_input):
    for key in responses : 
        if key in user_input : 
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if preprocess_input(user_input) == "bye" :
            print("Chatbot: " + random.choice(responses["bye"]))
            break

        response = get_response(preprocess_input(user_input)) 
        print("Chatbot: " , response)

if __name__ == "__main__":
    chat()