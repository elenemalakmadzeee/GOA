# ჩატ-ბოტი
is_running = True

while is_running:
    user_input = input("How are you? ")

    if user_input == "Normal":
        print("Bot: I hope you will get better.")
    elif user_input == "Great":
        print("Bot: Good! Have a nice day.")
        is_running = False  
    elif user_input == "Sad" or user_input == "Super Sad":
        print("Bot: It's sad.")
    else:
        print("Bot: Sorry, I didn't understand, repeat.")

print("Good bye!")
