def fibonnaci(n):
    assert n >= 0 and int(
        n) == n, "Fibonacci number cannot be negative or non integer"
    if n in [0, 1]:
        return n
    return fibonnaci(n-1)+fibonnaci(n-2)


# print(fibonnaci(1))
# print(fibonnaci(2))
# print(fibonnaci(3))
# print(fibonnaci(4))
# print(fibonnaci(5))
# print(fibonnaci(6))
# print(fibonnaci(7))
print(fibonnaci(8))
print(fibonnaci(-1))
