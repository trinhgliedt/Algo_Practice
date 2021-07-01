# How to find greatest common divisor of 2 numbers using recursion?
def gcd(a, b):
    assert int(a) == a and int(b) == b, "Numbers have to be integer"
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(48, -18))
# iterate from 1 to square root of a,
