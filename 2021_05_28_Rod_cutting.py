def rodCutting(n, p):
    # n is number of pieces in the rod
    # p is a list of the prices for the associated length
    if n == 0 or len(p) == 0:
        return 0
    pList = [0] + p
    # print(pList)
    # Make our table with n+1 number of row and n+1 number of column
    # priceTable = [[0]*(n+1)]*len(pList)
    priceTable = [[0]*(n+1) for _ in range(len(pList))]
    # print(priceTable)
    for i in range(1, len(pList)):
        for j in range(1, n+1):
            if i <= j:
                priceTable[i][j] = max(
                    priceTable[i-1][j], pList[i] + priceTable[i][j-i]
                )
            else:
                priceTable[i][j] = priceTable[i-1][j]
    # show result
    col_index = n
    row_index = len(pList) - 1
    # print(priceTable, col_index, row_index)
    while col_index > 0 or row_index > 0:
        # we have to compare the items right above each other
        # if they are the same values then the given row (piece) is not in the solution
        if priceTable[row_index][col_index] == priceTable[row_index-1][col_index]:
            # if priceTable[row_index][col_index] == priceTable[row_index-1][col_index]:
            row_index = row_index - 1
        else:
            print("We take piece with length: ", row_index, "m")
            col_index = col_index - row_index

    return priceTable[len(pList)-1][n]


# print(rodCutting(5, [2, 5, 7, 3, 9]))
# print(rodCutting(8, [3, 5, 8, 9, 10, 17, 17, 20]))
print(rodCutting(8, [1, 5, 8, 9, 10, 17, 17, 20]))
