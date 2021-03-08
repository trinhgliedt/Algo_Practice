from game_data import data
from replit import clear
from art import logo, vs
import random
# Pick out 2 random items to compare
pick_A = random.choice(data)
to_continue = True
score = 0

while to_continue == True:
    pick_B = random.choice(data)

    # If item B is the same as item A, repick until B is different than A
    while pick_B["name"] == pick_A["name"]:
        pick_B = random.choices(data)

    # Find out whether A or B has more followers
    answer = "a"
    if pick_A["follower_count"] < pick_B["follower_count"]:
        answer = "b"

    print(logo)
    print(
        f'Compare A: {pick_A["name"]}, {pick_A["description"]}, from {pick_A["country"]}.')
    print(pick_A["follower_count"])
    print(vs)
    print(
        f'Against B: {pick_B["name"]}, {pick_B["description"]}, from {pick_B["country"]}.')
    print(pick_B["follower_count"])
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == answer:
        score += 1
        clear()
        print(
            f"You're right! Current score: {score}\n----------------------------")
        pick_A = pick_B
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        score = 0
        to_continue = False
