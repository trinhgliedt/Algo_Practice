# 809. Expressive Words
# Medium

# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

# Given a list of query words, return the number of words that are stretchy. 

 

# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

# Constraints:

# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters
import re
class Solution(object):
    def expressiveWords(self, S, words):
        # :type S: str
        # :type words: List[str]
        # :rtype: int
        test_string = S
        # make a frequency table from the given string
        sMap = {}
        for c in S:
            if c not in sMap:
                sMap[c] = 1
            else: 
                sMap[c] += 1
        # then, make a frequency table from each words
        # the if the string has fewer of each character than each word then it's not a match
        resultList = []
        res = 0
        for word in words:
            if len(word) >= len(S):
                return 0
            wMap = {}
            countOfMatch1 = 0
            countOfMatch3 = 0
            for c in word:
                if c not in wMap:
                    wMap[c] = 1
                else: 
                    wMap[c] += 1
                # check to see if the character is in the given string
                pattern1 = c + "{"+"1"+"}"
                match1 = True if re.search(pattern1, test_string) else False
                if match1 == True: 
                    countOfMatch1 += 1
                match3 = False
                if match1 == True:
                    pattern3 = c + "{3,100}"
                    match3 = True if re.search(pattern3, test_string) else False
                    if match3 == True: 
                        countOfMatch3 += 1
            checkKey = []
            for key in wMap:
                if key in sMap:
                    if wMap[key] < sMap[key] and sMap[key] < 3:
                        checkKey.append(False)
                    elif sMap[key] < wMap[key]:
                        checkKey.append(False)
                    else:
                        checkKey.append(True)
            for key in sMap:
                if key not in wMap:
                    checkKey.append(False)
                # print("character: ", c, ", match 1: ", match1, ", match 3: ", match3)
            if countOfMatch1 == len(word) and countOfMatch3 > 0 and all(checkKey):
                res += 1
            print("countOfMatch1: ", countOfMatch1, ", countOfMatch3 : ", countOfMatch3, ", sMap: ", sMap, ", wMap:", wMap, ", checkKey:", checkKey)


            
        return res
            

s = Solution()
# print(s.expressiveWords("heeellooo", ["hello", "hi", "helo"]))
# print(s.expressiveWords("zzzzzyyyyy", ["zzyy","zy","zyy"]))
# print(s.expressiveWords("aaa", ["aaaa"]))
# print(s.expressiveWords("heeelllooo", ["hellllo"]))
print(s.expressiveWords("aaabbbaaa", ["a"]))

# We maintain a helper,
# that turns each string
# into a list of characters,
# and a list of counts of the length of the characters.

# We then compare the decomposition to the decomposition of the words in the list.

# When we decompose,
# we maintian a prev character starting with None,
# and append and update when we iterate over the string.

# When we compare,
# we first check the string,
# then we check the counts of the characters, when we iterate over the list of numbers.

class Solution1:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def decompose(s):
            prev = None
            res1 = ""
            res2 = []
  
            for ch in s:
                if ch != prev:
                    res1 += ch
                    res2.append(1)
                    prev = ch
                else:
                    res2[-1] += 1
            return res1, res2
                    
        def compare(p1, p2):
            if p1[0] == p2[0]:
                for i, v1 in enumerate(p1[1]):
                    v2 = p2[1][i] 
                    if v1 >= max(3, v2) or v1 == v2:
                        pass
                    else:
                        return False
                else:
                    return True
            else:
                return False

        S = decompose(S)
        return sum(compare(S, decompose(word)) for word in words)