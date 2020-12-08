# Suppose you want to convert an integer to a string in some base between binary and hexadecimal.
# For example, convert the integer 10 to its string representation in decimal as “10,” or
# to its string representation in binary as “1010.” While there are many algorithms to solve this
# problem, including the algorithm discussed in the stack section, the recursive formulation of
# the problem is very elegant.
def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(int(n / base), base) + convert_string[n % base]

print(to_str(10, 3))