# Page 67 Algo:
# Parens Valid
# Create a function that, given an input string,
# returns a boolean whether parentheses in that
# string are valid. Given input "y(3(p)p(3)r)s" ,
# return true. Given "n(0(p)3" , return false .
# Given "n)0(t(0)k" , return false .
def parensValid(str):
    count = 0
    for i, v in enumerate(str):
        if v == "(":
            if count < 0:
                return False
            count += 1
        elif v == ")":
            count -= 1
    return True if count == 0 else False

print(parensValid("y(3(p)p(3)r)s")) #true
print(parensValid("n(0(p)3")) # false
print(parensValid("n)0(t(0)k")) #false
print(parensValid("()(()(())))")) #false