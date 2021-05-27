# O(n2)
def fibonacci1(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci1(n-1, b, a+b)

# O(n2)


def fibonacci2(n):
    fib = [0]*n
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        fib[0], fib[1], fib[2] = 0, 1, 1
    for i in range(3, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[-1]


def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

# top-down approach
# O(n)


def fibonacci_memorization(n, table):
    if n not in table:
        table[n] = fibonacci_memorization(
            n-1, table) + fibonacci_memorization(n-2, table)
    return table[n]

# bottom-up approach
# O(n)


def fibonacci_tabulation(n, table):

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]


table = {0: 0, 1: 1}
# print(fibonacci_memorization(5, table))
print(fibonacci_tabulation(5, table))
