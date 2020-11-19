# Page 57 algo book
# Tricky Tribonacci
# Why stop with fibonacci? Create a function to
# retrieve a “tribonacci” number, from the sum of
# the previous 3 . Tribonaccis are {0, 0, 1, 1, 2, 4, 7,
# 13, 24, 44, 81, ...}. Again, use a time-space
# tradeoff to make this fast.
def tribonacci(x):
    current = 1; prev1 = 0; prev2 = 0; temp = 0; temp1 = 0
    for i in range (x, 1, -1):
        temp = current
        temp1 = prev1
        current = current + prev1 + prev2
        prev1 = temp
        prev2 = temp1
    return prev1

print("0: ", tribonacci(0));
print("1: ", tribonacci(1));
print("2: ", tribonacci(2));
print("3: ", tribonacci(3));
print("4: ", tribonacci(4));
print("5: ", tribonacci(5));
print("6: ", tribonacci(6));
print("7: ", tribonacci(7));
print("8: ", tribonacci(8));
print("9: ", tribonacci(9));
print("10: ", tribonacci(10));