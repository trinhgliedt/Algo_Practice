# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
# You can perform the following operations on the string, :

# Capitalize zero or more of 's lowercase letters.
# Delete all of the remaining lowercase letters in .
# Given two strings,  and , determine if it's possible to make  equal to  as described. If so, print YES on a new line. Otherwise, print NO.

# For example, given  and , in  we can convert  and delete  to match . If  and , matching is not possible because letters may only be capitalized or discarded, not changed.
from collections import Counter


def abbreviation(a, b):
    if len(b) > len(a):
        return "NO"
    aMap = Counter(a)
    bMap = Counter(b)

    for char, fre in bMap.items():
        if fre < aMap[char]:
            # there are more uppercase characters in a then b
            return "NO"

    for char in aMap.keys():
        if char == char.upper() and char not in bMap:
            return "NO"

    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i].upper() == b[j]:
            print(a[i], b[j])
            # found a match
            j += 1
        i += 1
    # print(j)
    if j == len(b):
        return "YES"
    else:
        return "NO"


def abbreviation(a, b):
    A = [[None for j in range(len(b))] for i in range(len(a))]
    # construct base cases
    # for our base case it's only going to be true if it's all lower case
    # and one of them is equal to B[0]
    # or there's only been one upper case letter and it's equal to b[j]
    # upper_encountered means that we encountered that upper case letter
    j = 0
    if a[0].upper() == b[0]:
        A[0][0] = True
    upper_encountered = a[0].isupper()
    for i in range(1, len(a)):
        if a[i].isupper() and upper_encountered:
            A[i][j] = False
        elif a[i].isupper() and not upper_encountered and a[i] == b[j]:
            A[i][j] = True
            upper_encountered = True
        elif a[i].isupper() and not upper_encountered and a[i] != b[j]:
            A[i][j] = False
            upper_encountered = True
        elif a[i].islower() and a[i].upper() == b[j] and not upper_encountered:
            A[i][j] = True
        # a[i].islower()
        else:
            A[i][j] = A[i-1][j]
        # print(A)
    # since a[i] is only length 1 anything in A[0][1:] will be False
    i = 0
    for j in range(1, len(b)):
        A[i][j] = False
    # now find the solution
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i].upper() == b[j] and a[i].islower():
                A[i][j] = A[i-1][j-1] or A[i-1][j]
            elif a[i].upper() == b[j] and a[i].isupper():
                A[i][j] = A[i-1][j-1]
            elif a[i].upper() != b[j] and a[i].islower():
                A[i][j] = A[i-1][j]
            else:
                A[i][j] = False
            print(A)
    if A[len(a)-1][len(b)-1]:
        return "YES"
    return "NO"


# print(abbreviation("daBcd", "ABC"))
print(abbreviation("DaBcd", "ABC"))
# print(abbreviation("daAABbBcCd", "ABC"))
# print(abbreviation("dBacd", "ABC"))
# str = "hHhAhhcahhacaccacccahhchhcHcahaahhchhhchaachcaCchhchcaccccchhhcaahhhhcaacchccCaahhaahachhacaahhaachhhaaaCalhhchaccaAahHcchcazhachhhaaahaahhaacchAahccacahahhcHhccahaachAchahacaahcahacaahcahacaHhccccaahaahacaachcchhahhacchahhhaahcacacachhahchcaAhhcaahchHhhaacHcacahaccccaaahacCHhChchhhahhchcahaaCccccahhcaachhhacaaahcaaaccccaacaaHachaahcchaahhchhhcahahahhcaachhchacahhahahahAahaAcchahaahcaaaaahhChacahcacachacahcchHcaahchhcahaachnachhhhcachchahhhacHhCcaHhhhcaCccccaaahcahacahchahcaachcchaachahhhhhhhhcahhacacCcchahccaaaaaHhhccaAaaaCchahhccaahhacaccchhcahhcahaahhgacahcahhchcaaAccchahhhaahhccaaHcchaccacahHahChachhcaaacAhacacaacacchhchchacchchcacchachacaahachccchhhaccahcacchaccaahaaaccccccaaaaaaaHhcahcchmcHchcchaaahaccchaaachchHahcaccaaccahcacacahAhaacaacaccaccaaacahhhcacAhaCchcaacCcccachhchchcchhchahchchahchchhchcacaachahhccacachaAhaaachchhchchchhaachahaahahachhaaaccacahhcacchhhaaachaaacAahhcachchachhhcacchacaaChCahhhccahChaachhcahacchanaaacchhhccacacchcahccchAcahacaaachhacchachccaaHacaacAhahcCh"
# pat = "HAHHCHAACCCAHCHHAHHAHCACCHCCHHCAAHHCACCCAHHHACAAHHHHCHHCAHHAHHAAAHAACAAHAHHCAHAHACHACHCHACACHAAHHAAAHCAHHACACAACHHHCHAHCAHCHHHAHAHACCAAAHCHHCHHCCAACCCCAACHACAACAAHACHCHAHHACCHCAHHHAAACHACAACHCACACAHHCCHAHACCCACCAACHCHHHCCCCCHCCAHHCAAHHAHHHHHHHAACCCCAHCCAAAAAHHHAAAACCAHHCAHACACCHHCHAHAHHCHAACHHHHHCCHCCAHAHCHCAAACCACCCCHACCACHHACHHACACHACCAACCCCAAAAHHAHCHHHCCAHCCHACHHAHCCACACCHAHAAACACCCCAHCCAHACCCCCCHCCHHCHHHHCHCHCAHHHACHAHAACCCAAAACHAACAAAHHAAHAAAHACHHCACHCCHCHAACHACACHHCCCCCAHCACHAAAHCHCAHACAAC"
# print(abbreviation(str, pat))
