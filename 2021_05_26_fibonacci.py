
def fibonacci1(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibonacci(n-1, b, a+b)


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
    return fib


def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b


print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
