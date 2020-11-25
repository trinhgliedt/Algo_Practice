# Hacker Rank:
# Designer PDF Viewer:
# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

# PDF-highighting.png

# There is a list of  character heights aligned by index to their letters. For example, 'a' is at index  and 'z' is at index . There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are  wide.

# Example
 

# The heights are t=2 and o=1. The tallest letter is  high and there are  letters. The hightlighted area will be  so the answer is .

# Function Description

# Complete the designerPdfViewer function in the editor below.

# designerPdfViewer has the following parameter(s):

# int h[26]: the heights of each letter
# string word: a string
# Returns

# int: the size of the highlighted area
# Input Format

# The first line contains  space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
# The second line contains a single word consisting of lowercase English alphabetic letters.

# Constraints

# , where  is an English lowercase letter.
#  contains no more than  letters.
# Sample Input 0

# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
# Sample Output 0

# 9
# Explanation 0

# We are highlighting the word abc:

# Letter heights are t=2, o = 1, r=1 ,  and . The tallest letter is 2, is  high. The selection area for this word is .

# Note: Recall that the width of each character is .

# Sample Input 1

# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
# zaba
# Sample Output 1

# 28
# Explanation 1

# The tallest letter in  is  at . The selection area for this word is .
# https:#www.hackerrank.com/challenges/designer-pdf-viewer/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def designerPdfViewer(h, word):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    # make a hashmap of the given height array:
    hashMap = {};
    for i in range(0,26):
        hashMap[alphabet[i]] = h[i]
    
    # iterate through the word to count the character and find max height:
    count = 0; maxH = 0
    for i in range(0,len(word)):
        count += 1
        if maxH < hashMap[word[i]]:
            maxH = hashMap[word[i]];
    
    return (maxH*count);


print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7], "zaba"));