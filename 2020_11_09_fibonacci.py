# Fibonacci
# Implement the Fibonacci function, a famous mathematical equation that generates a numerical
# sequence such that each number is the sum of the previous two. The Fibonacci numbers at index 0
# and 1, coincidentally, have values of 0 and 1. Your function should accept an argument of which
# Fibonacci number.
# Examples: fibonacci(2) = 1, fibonacci(3) = 2, fibonacci(4) = 3, fibonacci(5) = 5, etc.
def fibonacci(x):
    if x <= 1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)
# print(fibonacci(12))

def fibonacci1(x):
    a = 1
    b = 0
    temp = 0
    for i in range (x+1):
        temp = a
        a = a + b
        b = temp
    return b
# print(fibonacci1(12))

def fibonacci2(x):
    a = 1
    b = 0
    temp = 0
    while x >= 0:
        temp = a
        a = a + b
        b = temp
        x = x - 1
    return b
print(fibonacci2(12))