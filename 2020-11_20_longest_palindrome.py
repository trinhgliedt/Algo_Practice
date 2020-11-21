# Page 68
# Longest Palindrome
# For this challenge, we will look not only at the
# entire string, but also substrings within it.
# For a string, return the longest palindromic
# substring. Given "what up, dada?" , return
# "dad" . Given "not much" , return "n" . Include
# spaces as well (i.e. be strict, as in the “Is
# Palindrome” challenge): given "My favorite
# racecar erupted!" , return "e racecar e" .
def isPalindrome(str):
    backwardsString = ""
    for v in reversed(str):
        backwardsString += v
    return backwardsString == str

def longestPalindrome(str):
    prevPalindrome = currPalindrome = ''
    for i, v1 in enumerate(str):
        for j in range(len(str)-1, -1, -1):
            if isPalindrome(str[i:j]):
                if len(prevPalindrome) < len(str[i:j]):
                    prevPalindrome = str[i:j]
                break
    return prevPalindrome

print(longestPalindrome('this')) # should log 't'
print(longestPalindrome('bobe')) # should log 'bob'
print(longestPalindrome('what up, daddy-o?')) # should log 'dad'
print(longestPalindrome('Yikes! my favorite racecar erupted!'))  # should log 'e racecar e'