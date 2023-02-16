import math

def issquare(n):
    
    if n < 0:
        return False
    elif n == 0:
        return True
    elif isinstance(math.sqrt(n), int):
        return True
    

print(issquare( 25))