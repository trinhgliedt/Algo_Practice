# Page 53 algo book
# Remove Negatives
# Implement a function removeNegatives() that
# accepts an array and removes any values that
# are less than zero.
# Second-level challenge: don’t use nested loops.
def removeNegatives(li):
    for item in li: 
        if item < 0: 
           li.remove(item) 
    return li
    print(li)

print(removeNegatives([-2,3,5,-9,5,2,-6]))

# Using list comprehension:
# https://www.programiz.com/python-programming/list-comprehension
def removeNegatives2(li):
    return [num for num in li if num >=0 ] 
print(removeNegatives2([-2,3,5,-9,5,2,-6]))