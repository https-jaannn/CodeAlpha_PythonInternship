# Basic Rule-Based Chatbot

def get_reply(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"
    elif "how are you" in message:
        return "I'm fine, thank you! How are you?"
    elif "your name" in message or "who are you" in message:
        return "I'm PyBot, a simple Python chatbot."
    elif "thank" in message:
        return "You're welcome!"
    elif "help" in message:
        return "You can say hello, ask how I am, or type bye to exit."
    elif message in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that yet. Try saying 'help'."


print("=== PYBOT: BASIC CHATBOT ===")
print("Type 'help' for examples, or 'bye' to stop.")

while True:
    user_message = input("You: ")
    reply = get_reply(user_message)
    print("PyBot:", reply)

    if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break
