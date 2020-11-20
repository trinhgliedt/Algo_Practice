# Page 66 Algo:
# Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given
# "0s1a3y5w7h9a2t4?6!8?0" , the function should return the number 1,357,924,680.
def strDigits(str):
    newStr = ""
    for i in str:
        if i.isnumeric():
            newStr += i
    return int(newStr)
print(strDigits("0s1a3y5w7h9a2t4?6!8?0"))
