def is_square(n):
    if n == 0:
        return True
    if n < 0:
        return False
    
    if n % 10 == (1, 4, 5, 6, 9, 00):
        return True
    elif n % 10 == (1,4,9) and n%100 == (0,2,4,5,8):
        return True
    elif n % 10 == 5 and n%100 == 2:
        return True
    elif n % 10 == 6 and n%100 == (1,3,5,7,9):
        return True
    else:
        return False

print(36%100)
#print(is_square(36))