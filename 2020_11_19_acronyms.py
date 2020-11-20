# Page 66 algo:
# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). Given
# "there's no free lunch - gotta pay yer way" , return "TNFL-GPYW" . Given "Live
# from New York, it's Saturday Night!" , return "LFNYISN" .
def acronyms(str):
    arr = str.split()
    newStr = ""
    for word in arr:
        newStr += word[0].upper()
    return newStr
print(acronyms("Live from New York, it's Saturday Night!"))