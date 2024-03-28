import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def print_result(user_choice, computer_choice, outcome):
    print("User's choice:", user_choice)
    print("Computer's choice:", computer_choice)
    if outcome == "win":
        print("You win!")
    elif outcome == "lose":
        print("You lose!")
    else:
        print("It's a tie!")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        outcome = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, outcome)

        if outcome == "win":
            user_score += 1
        elif outcome == "lose":
            computer_score += 1

        print("Score: User -", user_score, "Computer -", computer_score)

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

