# How to find the sum of digits of a positive integer number using recursion?

def sumDigit(n):
    assert n >= 0 and int(n) == n, "The number has to be a positive integer "
    if n == 0:
        return 0
    else:
        return sumDigit(n//10) + n % 10


m = 56231
m = -1
print(sumDigit(m))
