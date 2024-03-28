import random
import string

def generate_password(length, difficulty):
    if difficulty == "easy":
        characters = string.ascii_letters + string.digits
    elif difficulty == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif difficulty == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.punctuation
    else:
        print("Invalid difficulty level. Defaulting to medium difficulty.")
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length should be a positive integer.")
            return
        difficulty = input("Enter the difficulty level (easy, medium, hard): ").lower()
        password = generate_password(length, difficulty)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
