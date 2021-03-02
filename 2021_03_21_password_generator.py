# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pw = ""
pw2 = ""
pw_list = []
for i in range(1, nr_letters+1):
    letter = random.choice(letters)
    pw += letter
    pw_list.append(letter)

for i in range(1, nr_symbols+1):
    symbol = letter = random.choice(symbols)
    pw += symbol
    pw_list.append(symbol)

for i in range(1, nr_numbers+1):
    number = letter = random.choice(numbers)
    pw += number
    pw_list.append(number)
random.shuffle(pw_list)
pw2 = "".join(pw_list)
print(pw, "\n", pw2)
