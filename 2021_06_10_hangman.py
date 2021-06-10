import random

lives = 6
end_of_game = False
word_list = ['leopard', 'elephant', 'space']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# create blank
display = []
for _ in range(word_length):
    display += "_"

guessed_letters = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in guessed_letters:
        guessed_letters.append(guess)
    else:
        print(f"You already guessed {guess}")

    # check guessed letter:
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # check if user is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not a match. You lose a life. Lives left: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose!")

    # print out the current progress: print out the display list:
    print(" ".join(display))

    # check if the user has gotten all letters:
    if "_" not in display:
        end_of_game = True
        print("You win!")
