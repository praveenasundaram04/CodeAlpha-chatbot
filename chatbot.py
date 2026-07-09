print("===Welcome to My chatbot===")

while True:
    user=input("You:").lower()
    if user=="hello":
        print("Bot:Hi!how can I help you?")
    elif user=="how are you":
        print("Bot:I am fine.Thank you!")
    elif user=="What is your name":   
        print("Bot:My name is CodeBot.")
    elif user=="bye":
        print("Bot:Goodboy!Have a nice day!")
        break
    else:
        print("Bot:Sorry,I don't understand.")
        