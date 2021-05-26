# https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming

def abbreviation(a, b):
    if len(b) > len(a):
        print("NO")
        return

    else:
        charList = []
        for char in b:
            if char.lower() not in a.lower():
                return "NO"
            else:
                charList.append(a.lower().index(char.lower()))
        check = []
        for i in range(len(charList)-1):
            if charList[i] > charList[i+1]:
                return "NO"
            else:
                check.append(True)
        if all(check):
            return "YES"


# abbreviation("daBcd", "ABC")
# abbreviation("dBacd", "ABC")
