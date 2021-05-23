# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]


# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution(object):
    def letterCombinations(self, digits):
        # """
        # :type digits: str
        # :rtype: List[str]
        # """
        pDict = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: [
            "g", "h", "i"], 5: ["j", "k", "l"], 6: [
                "m", "n", "o"], 7: ["p", "q", "r", "s"], 8: [
                    "t", "u", "v"], 9: ["w", "x", "y", "z"]}
        if len(digits) == 0:
            return ""
        elif len(digits) == 1:
            return pDict[int(digits)]
        else:
            result, heads, tails = [], [], []
            for char in digits:
                digit = int(char)
                tails = pDict[digit]
                tempResult = []
                if len(heads) == 0:
                    tempResult = pDict[digit]
                else:
                    for head in heads:
                        for tail in tails:
                            tempResult.append(head+tail)
                            # print(tempResult)
                heads = tempResult
            # print(digit, heads, tails, tempResult)
            result = heads
            return result


sol = Solution()
# print(sol.letterCombinations("23"))
# print(sol.letterCombinations(""))
# print(sol.letterCombinations("2"))
print(sol.letterCombinations("2345"))
# print("a"+"b")
