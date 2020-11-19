# Page 65 Algo book
# ReverseString
# Implement a function reverseString(str) that, given a string, will return the string of the same length but
# with characters reversed. Example: given "creature" , return "erutaerc" . Do not use the built-in
# reverse() function!
def reverseStr(str):
    newStr = ""
    for i in reversed(str):
        newStr += i
    return newStr
print(reverseStr("trinh"))
