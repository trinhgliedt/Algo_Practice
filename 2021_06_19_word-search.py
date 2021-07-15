# https://leetcode.com/problems/word-search/
# Medium
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false


# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


# Follow up: Could you use search pruning to make your solution faster with a larger board?
class Solution:
    # dx represents the change of positions that we can go to for axis
    dx = [0, 0, -1, 1]
    # dy represents the change of positions that we can go to for y axis
    dy = [1, -1, 0, 0]

    def solution(self, board, word, x, y, cur):
        # if the current position is out of bounds of the board, or if current char is visited, return False
        if(x < 0 or x >= len(board) or y < 0 or y >= len(board[x]) or board[x][y] == ' '):
            return False
        cur += board[x][y]
        #  if current string is longer than the word, return False
        if(len(cur) > len(word)):
            return False
        # if the last character of the current string is different than character of the word at the same position, return False
        if(cur[len(cur)-1] != word[len(cur)-1]):
            return False
        if(cur == word):
            return True
        # save the current value of board[x][y] to a variable and assign another value to board[x][y] to indicate it's visited
        temp = board[x][y]
        # empty char represents a cell that has been visited
        board[x][y] = ' '

        # 4 is the number of neighboring cells, vertical (up, down), and horizontal (left, right)
        for i in range(4):
            # inside the loop, check if the result of recursively calling the solution function with the same set of params except this time, we would change the x, y positions to indicate visiting neighbors
            if(self.solution(board, word, x+self.dx[i], y+self.dy[i], cur)):
                return True

        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        if(len(word) == 0):
            return True
        n = len(board)
        # loop through the board to find a match for the first character of word
        for i in range(n):
            m = len(board[i])
            for j in range(m):
                # start with an empty current string
                if(word[0] == board[i][j] and self.solution(board, word, i, j, "")):
                    return True
        return False
