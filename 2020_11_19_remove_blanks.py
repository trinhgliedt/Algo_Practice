# Page 66 algo book:
# Remove Blanks
# Create a function that, given a string, returns the string, without blanks. Given " play that
# Funky Music " , returns a string containing "playthatFunkyMusic" .
def removeBlanks(str):
    return "".join(str.strip().split())

print(removeBlanks("  Play    that Funky Music  "))