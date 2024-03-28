import random

def roll_dice(num_sides, num_rolls):
    print(f"Rolling a {num_sides}-sided dice {num_rolls} times:")
    for roll in range(1, num_rolls + 1):
        result = random.randint(1, num_sides)
        print(f"Roll {roll}: {result}")

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_sides = int(input("Enter the number of sides on the dice: "))
            if num_sides <= 0:
                print("Please enter a positive number of sides.")
                continue
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                print("Please enter a positive number of rolls.")
                continue
            roll_dice(num_sides, num_rolls)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        finally:
            play_again = input("Do you want to roll again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thank you for using the Dice Rolling Simulator!")
                break

if __name__ == "__main__":
    main()
