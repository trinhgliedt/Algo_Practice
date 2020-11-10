# Page 53 algo book:
# Skyline Heights
# You are given an array with heights of consecutive buildings in the city. For example, [-1,7,3] would
# represent three buildings: first is actually below street level, second is seven stories high, and third is
# three stories high (but hidden behind the seven-story onbe). You are situated at street level. Return an
# array containing heights of the buildings you can see, in order. Given [1,-1,7,3] return [1,7] .
def visibleBuildings(li):
    result = []
    for item in li:
        if item > 0 and len(result) == 0:
            result.append(item)
        elif item > 0 and item > result[len(result)-1]:
            result.append(item)
    return result
print(visibleBuildings([1,-1,7,3,10,5,-1,11]))
print(visibleBuildings([-1,-2,3]))