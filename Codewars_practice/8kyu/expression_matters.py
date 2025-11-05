a = 1
b = 2
c = 3

def expression_matter(a, b, c):
    for i in a,b,c:
        return max(a*b*c, a+b+c, a*b+c, a+b*c, a*(b+c), (a+b)*c,)
    
print(expression_matter(a,b,c))