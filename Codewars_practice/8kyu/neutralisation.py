def neutralise(s1, s2):
    
    s1list = list(s1)
    s2list = list(s2)
    result = []
    
    for i in range(len(s1list)):
        if s1list[i] == "+" and s2list [i] == "+":
            result.append("+")
        elif s1list[i] == "-" and s2list [i] == "-":
            result.append("-")
        else:
            result.append("0")
    
    stringresult = "".join(result)
    return stringresult

s1 = "-+-+-+"
s2 = "++--++"
print(neutralise(s1, s2))