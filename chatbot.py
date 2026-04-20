print("Hello! I am your chatbot. Type 'bye' to exit.")

responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing great!",
    "what is your name": "I am a simple chatbot.",
    "bye": "Goodbye!"
}

while True:
    user_input = input("You: ").lower()

    if user_input in responses:
        print("Bot:", responses[user_input])
        
        if user_input == "bye":
            break
    else:
        print("Bot: Sorry, I don't understand.")
