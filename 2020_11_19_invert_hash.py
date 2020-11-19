# page 65 algo book
# InvertHash
# Create invertHash(assocArr) that converts a hash’s keys to values and values to corresponding keys.
# Example: given {"name": "Zaphod"; "numHeads": 2} , return {"Zaphod":
def invertHash(dict):
    newDict = {}
    for key, val in dict.items():
        newDict[val] = key
    return newDict

print(invertHash({"name": "Zaphod", "numHeads": 2}))