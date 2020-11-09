# Page 41 algo books
# Sum To One Digit
# Implement a function sumToOne(num) that,
# given a number, sums that number’s digits
# repeatedly until the sum is only one digit. Return
# that final one digit result.
def sumToOneDigit(num):
    numStr = str(num)
    numL = len(numStr)
    tempNum = 0

    while (numL > 1):
        tempNum = 0
        for i in range(numL):
            tempNum += int(numStr[i])
        numStr = str(tempNum)
        numL = len(numStr)
    return tempNum
print(sumToOneDigit(945))
# print(sumToOneDigit(945+1))
# print(sumToOneDigit(945+2))
# print(sumToOneDigit(945+3))
# print(sumToOneDigit(945+4))
# print(sumToOneDigit(945+5))
# print(sumToOneDigit(945+6))
# print(sumToOneDigit(945+7))
# print(sumToOneDigit(945+8))
# print(sumToOneDigit(945+9))

