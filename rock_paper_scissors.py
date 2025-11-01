import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("-----------------------------------")

    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user_choice == 'exit':
            print("👋 Thanks for playing! Goodbye!")
            break

        if user_choice not in options:
            print("⚠️ Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"🖥️ Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win!")
        else:
            print("💻 Computer wins!")

        print("-----------------------------------")

if __name__ == "__main__":
    rock_paper_scissors()
