# Page 64 algo book
# Arrs2Map
# Given two arrays, create an associative array (map) containing keys of the first, and values of the
# second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true] , return {"abc":
# 42, 3: "wassup", "yo": true} .
def arrayToMap(arr1, arr2):
    newMap = {}
    for a, b in zip(arr1, arr2):
        newMap[a] = b
    return newMap
print(arrayToMap(["abc", 3, "yo"],[42, "wassup", True]));
print(arrayToMap(["abc", 3, "yo"],[42, "wassup", True, 5, 6, 7]));