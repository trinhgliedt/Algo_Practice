def binary_search(container, item, left, right):
    if right < left:
        return -1
    middle = (left+right)//2
    if container[middle] == item:
        return middle
    elif container[middle] < item:
        print("checking on the right...")
        return binary_search(container, item, middle+1, right)
    elif container[middle] > item:
        print("checking on the left...")
        return binary_search(container, item, left, middle-1)


arr = [-5, -3, 0, 6, 8, 10, 80]
print(binary_search(arr, 10, 0, len(arr)-1))
print(binary_search(arr, 50, 0, len(arr)-1))
