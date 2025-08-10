import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors!")
    player = input("Enter your choice (rock, paper, scissors): ").lower()

    if player not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    bot = random.choice(choices)
    print(f"🤖 Bot chose: {bot}")

    if player == bot:
        print("It's a draw! 🤝")
    elif (player == "rock" and bot == "scissors") or \
         (player == "paper" and bot == "rock") or \
         (player == "scissors" and bot == "paper"):
        print("🎉 You win!")
    else:
        print("💀 You lose!")

rock_paper_scissors()
