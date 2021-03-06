############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
card_deck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


def card_value(card):
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 11
    else:
        return card


def draw_a_card(cards):
    """Pick a random card and add it to a user/dealer hand"""
    import random
    card_drawn = random.choices(card_deck)
    cards.append(card_drawn[0])
    return


def calculate_score(cards):
    score = 0
    count_of_A = 0
    for card in cards:
        if card == "A":
            count_of_A += 1
        score += card_value(card)
    # if score is > 21, reduce score by 10 in order to use 1 as value for A, not 11. Maximum actions are the number of A card in hand
    #print("count_of_A: ",count_of_A)
    for i in range(1, count_of_A + 1):
        if score > 21:
            score -= 10
    return score
#   problem:
#  Type 'y' to get another card, or type 'n' to pass: y
# Your cards: [5, 'A', 'A', 3, 2], current score: 12
# Computer's first card: 6
# Type 'y' to get another card, or type 'n' to pass: y
# Your cards: [5, 'A', 'A', 3, 2, 'J'], current score: 12


def inform_user_game_status(user_cards, user_score, dealer_cards):
    print(
        f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")
    return


def inform_dealer_busted(user_cards, user_score, dealer_cards):
    print(
        f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's cards are busted: {dealer_cards}. You win")
    return


def busted(cards):
    if calculate_score(cards) > 21:
        return True
    else:
        return False


def busted_msg(cards):
    print(f"Busted. Your score is over 21: {cards}. You lose")
    return


def is_21(cards):
    if calculate_score(cards) == 21:
        return True
    else:
        return False


def stop_game():
    print("Goodbye")
    return


def is_black_jack(cards):
    if calculate_score(cards) == 21:
        return True
    else:
        return False


def black_jack_msg(winner):
    if winner == "dealer":
        print("Computer got a black jack. You lose")
    elif winner == "player":
        print("You got a black jack. You win")
    return


def dealer_draw(cards):
    while calculate_score(cards) <= 16:
        draw_a_card(cards)
    return


def find_and_announce_winner(user_cards, dealer_cards):
    dealer_score = calculate_score(dealer_cards)
    user_score = calculate_score(user_cards)
    if dealer_score < user_score:
        status = "win"
    elif dealer_score > user_score:
        status = "lose"
    else:
        status = "tie with the computer"
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's cards: {dealer_cards}, score: {dealer_score}")
    print(f"You {status}")
    return
# Pick out 2 cards for player and 2 for dealer


def black_jack():
    from art import logo
    from replit import clear
    print(logo)
    new_game = "y"
    user_cards = []
    dealer_cards = []
    user_score = 0
    to_continue = "y"
    draw_a_card(user_cards)
    draw_a_card(user_cards)
    draw_a_card(dealer_cards)
    draw_a_card(dealer_cards)

    if is_black_jack(dealer_cards):
        black_jack_msg("dealer")
        # stop_game()
    else:
        inform_user_game_status(user_cards, user_score, dealer_cards)
        to_continue = input(
            "Type 'y' to get another card, or type 'n' to pass: ")
        while to_continue == "y":
            draw_a_card(user_cards)
            if busted(user_cards):
                busted_msg(user_cards)
                # stop_game()
                break
            else:
                inform_user_game_status(user_cards, user_score, dealer_cards)
                to_continue = input(
                    "Type 'y' to get another card, or type 'n' to pass: ")
        if not busted(user_cards):
            dealer_draw(dealer_cards)
            if busted(dealer_cards):
                inform_dealer_busted(user_cards, user_score, dealer_cards)
            else:
                find_and_announce_winner(user_cards, dealer_cards)
    new_game = input(
        "------------------------------------\nDo you want to play a another game of black jack? Type 'y' or 'n': ")
    if new_game == 'y':
        clear()
        black_jack()
    else:
        stop_game()


black_jack()
