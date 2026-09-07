print("🤖 ChatBot: Hello! I am your AI Chatbot.")
print("🤖 ChatBot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("ChatBot: Hello! How can I help you?")

    elif "how are you" in user:
        print("ChatBot: I am fine. Thank you for asking!")

    elif "your name" in user:
        print("ChatBot: My name is CodSoft ChatBot.")

    elif "help" in user:
        print("ChatBot: Sure! I can answer simple questions.")

    elif "thank" in user:
        print("ChatBot: You're welcome!")

    elif user == "bye":
        print("ChatBot: Goodbye! Have a nice day!")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")