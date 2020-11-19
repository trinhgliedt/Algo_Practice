# Page 56 algo book
# Shuffle
# Recreate the shuffle() built into JavaScript, to
# efficiently shuffle a given array’s values. Do you
# need to return anything from your function?
import random
def shuffle(arr):
    random.shuffle(arr)
    return arr

print(shuffle([1,2,3,4,5]))
print(shuffle([6,10,2,3,4]))
print(shuffle(["apple", "banana", "strawberry", "plum"]))
