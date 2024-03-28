import random

# List of words for the game
word_list = ["apple", "banana", "orange", "grape", "pear", "kiwi", "pineapple", "strawberry", "watermelon"]

def select_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def display_hangman(incorrect_guesses):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
        """,
        """
           --------
           |      |
           |      O
           |     
           |     
           |     
        """,
        """
           --------
           |      |
           |      
           |     
           |     
           |     
        """
    ]
    return stages[incorrect_guesses]

def hangman():
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = len(display_hangman(0)) // 11 - 1

    print("Welcome to Hangman!")
    print(display_hangman(incorrect_guesses))
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(display_hangman(incorrect_guesses))
            print("Incorrect guess! Try again.")

            if incorrect_guesses == max_attempts:
                print("You've run out of attempts. The word was:", word)
                break
        else:
            print(display_word(word, guessed_letters))

            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You've guessed the word:", word)
                break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    hangman()