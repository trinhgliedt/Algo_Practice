# Page 67:
# Braces Valid
# Given a string, returns whether the sequence of
# various parentheses, braces and brackets within
# it are valid. For example, given the input string
# "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!" , return
# true . Given "d(i{a}l[t]o)n{e" , return
# false . Given "a(1)s[O(n]0{t)0}k" , return
# false .
def bracesValid(str):
    open_braces = []
    for i, v in enumerate(str):
        if v == '(' or v == '{' or v == '[':
            open_braces.append(v)
        elif v == ')' or v == '}' or v == ']':
            if v == ")" and open_braces[-1] == "(" or v == "}" and open_braces[-1] == "{" or v == "]" and open_braces[-1] == "[":
                open_braces.pop()
            else:
                return False
    return len(open_braces) == 0
    
print(bracesValid("w(a{t}s[o(n{c}o)m]e)h[e{r}e]!")); #true
print(bracesValid('{[a()b]c}')); #true
print(bracesValid('{[()}]')); #false
print(bracesValid('{}[]()[(])')); #false
