from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.")
print(logo)
bids = []
to_continue = "yes"
max_bid = {}
max_amount = 0
while to_continue == "yes":

    bid = {}
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bid["name"] = name
    bid["amount"] = bid_amount
    if bid_amount > max_amount:
        max_amount = bid_amount
        max_bid["name"] = name
        max_bid["amount"] = max_amount
    bids.append(bid)
    to_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.").lower()
    clear()
print(f'The winner is {max_bid["name"]} with a bid of ${max_bid["amount"]}')
