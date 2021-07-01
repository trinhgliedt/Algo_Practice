def factorial(n):
    # if n < 0 or int(n) != n:
    #     return
    assert n >= 0 and int(n) == n, "The number must be positive integer only"
    if n in [0, 1]:
        return n
    else:
        return n*factorial(n-1)


print(factorial(1.5))
