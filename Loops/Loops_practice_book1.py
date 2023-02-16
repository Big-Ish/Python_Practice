product = 0

while True:
    num = int(input("Enter a number: "))
    multiplied = num * 10
    product += multiplied
    
    if product < 100:
        continue
    else:
        break
print("Sum:", product)
