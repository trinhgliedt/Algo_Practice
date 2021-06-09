# trying to add people to the boats
# given a people array and integer limit
# people array is an array of people's weights, i-th person has a weight people[i]. Each boat can carry at most limit
# each boat carries at most 2 people at the same time, given that their weight sum is at most limit
# Return the minimum number of boats to carry every given person
# note: it is guaranteed each person can be carried by a boat
# --> the maximum number of people a boat can carry is 2
# --> every individual person has a weight lower than or equal to limit
# --> worst case scenario is that it would take as many boats as there are people
def boats(peopleW, limit):
    # need to maximize the number of pairs of people whose weights can be added together in the same boats (sum of weights is lower or equal to the limit)
    peopleW.sort()
    boats = 0
    i, j = 0, len(peopleW)-1
    while i <= j:
        print(i, j, peopleW[i], peopleW[j])
        if i == j:
            boats += 1
            return boats
        if peopleW[i] + peopleW[j] <= limit:
            boats += 1
            i += 1
            j -= 1
        elif peopleW[i] + peopleW[j] > limit:
            boats += 1
            j -= 1
    return boats


arr = [3, 1, 2, 4, 5, 5, 3]
print(boats(arr, 5))
