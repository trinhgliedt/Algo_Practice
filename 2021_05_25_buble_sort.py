# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


def countSwaps(a):
    no_of_swaps = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                no_of_swaps += 1

    print(
        f"Array is sorted in {no_of_swaps} swaps.")
    print(
        f"First Element: {a[0]}")
    print(
        f"Last Element: {a[-1]}")
    return


print(countSwaps([6, 4, 1]))
print(countSwaps([9, 5, 3, 21, 8, 2, 1, 7, -50]))
