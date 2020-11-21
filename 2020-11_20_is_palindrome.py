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
    backwardsString = ""
    for v in reversed(str):
        backwardsString += v
    return backwardsString == str

print(isPalindrome("racecar"))
print(isPalindrome("Dad"))
print(isPalindrome("oho!"))