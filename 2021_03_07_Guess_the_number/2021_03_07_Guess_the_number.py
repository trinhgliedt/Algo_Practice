# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
NO_OF_GUESSES_DICT = {"easy": 10, "hard": 5}


def process_difficulty_input(difficulty):
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty not in ["easy", "hard"]:
            print("Invalid choice. Please choose again.")
    return difficulty


play_again = "y"

while play_again == "y":
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    import random
    secret_num = random.randint(1, 100)
    print(f"Pssst, the correct answer is {secret_num}")
    difficulty = ""
    difficulty = process_difficulty_input(difficulty)

    for no_of_guess in range(NO_OF_GUESSES_DICT[difficulty], 0, -1):
        print(
            f"You have {no_of_guess} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess != secret_num:
            if guess < secret_num:
                print("Too low.\nGuess again.")
            elif guess > secret_num:
                print("Too high.\nGuess again.")
            if no_of_guess == 1:
                print("You've run out of guesses, you lose.")
                play_again = input("Play again? Type 'y' or 'n': ")
        elif guess == secret_num:
            print(f"Congratulation! {guess} is the correct number. You won!")
            break
            play_again = input("Play again? Type 'y' or 'n': ")
