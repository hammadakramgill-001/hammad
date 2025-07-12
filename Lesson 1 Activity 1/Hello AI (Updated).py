# Greet the user
print("Hello! I am Hello AI, your chatbot friend. What's your name? : ")

# Get user input
name = input()

# Respond to user's name
print(f"Nice to meet you, {name}!")

# Ask about user's mood
print("How are you feeling today? (good or bad) : ")
mood = input().lower()

# Respond based on mood
if mood == "good":
    print("I'm glad to hear that.")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# Ask about user's hobby
print("What is your favorite hobby? : ")
hobby = input()
print(f"That sounds fun! I wish I could try {hobby} too!")

# Ask about favorite food
print("What's your favorite food? : ")
food = input()
print(f"Yum! I bet {food} tastes amazing!")

# End the conversation with a personal message
print(f"It was really nice chatting with you, {name}.")
print("Thanks for telling me about yourself. Have a great day!")
