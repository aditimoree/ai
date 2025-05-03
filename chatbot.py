def chatbot():
    print("Welcome to ShopBot! How can I help you today?")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("ChatBot: Thank you for visiting! Have a great day!")
            break
        elif "order" in user_input:
            print("ChatBot: You can check your order status by logging into your account.")
        elif "refund" in user_input:
            print("ChatBot: Refunds are processed within 5-7 business days.")
        elif "delivery" in user_input:
            print("ChatBot: Standard delivery takes 3-5 days. Express delivery is 1-2 days.")
        elif "help" in user_input or "support" in user_input:
            print("ChatBot: Sure! What do you need help with? Orders, refunds, delivery?")
        elif "hello" in user_input or "hi" in user_input:
            print("ChatBot: Hello! How can I assist you today?")
        else:
            print("ChatBot: Sorry, I didn't understand that. Can you please rephrase?")


chatbot()
