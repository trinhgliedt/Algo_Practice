# page 41 algorithm book
# Statistics to Doubles
# Implement a ‘die’ that randomly returns an
# integer between 1 and 6 inclusive. Roll a pair of
# these dice, tracking the statistics until doubles
# are rolled. Display the number of rolls , min , max ,
# and average .
import random, math

def statisticToDoubles():
    die1 = 0
    die2 = -1
    rollCount = 0
    while die1 != die2:
        die1 = math.floor(random.random()*6) + 1
        die2 = math.floor(random.random()*6) + 1
        print("die1: ", die1, ", die2: ", die2)
        rollCount += 1
    return rollCount

print(statisticToDoubles())