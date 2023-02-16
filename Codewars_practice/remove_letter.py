# Your goal is to create a function that removes the first and last characters of a string. 
# You're given one parameter, the original string. 
# You don't have to worry with strings with less than two characters.

def removechar(s):
    slist = []
    removed = ""
    
    for i in s[1 : len(s)-1]:
        slist.append(i)
    
    for j in slist:
        removed += j
        
    return removed

removechar(s = "N2/3@a")