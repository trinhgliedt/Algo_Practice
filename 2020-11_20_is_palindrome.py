# page 68
# Is Palindrome
# Strings like "Able was I, ere I saw
# Elba" or "Madam, I'm Adam" could be
# considered palindromes , because (if we ignore
# spaces, punctuation and capitalization) the letters
# are the same from front and back.
# Create a function that returns a boolean whether
# the string is a strict palindrome. For "a x a" or
# "racecar" , return true . Do not ignore spaces,
# punctuation and capitalization: if given "Dud" or
# "oho!" , return false .
def isPalindrome(str):
    if len(str) == 1:
        return True
    check = False;
    for i, v in enumerate(str):
        if v == str[-1-i]:
            check = True
        else:
            check = False
    return check

print(isPalindrome("racecar"))
print(isPalindrome("Dad"))
print(isPalindrome("oho!"))