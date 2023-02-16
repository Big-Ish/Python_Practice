def biggest():
    print('Biggest to Smallest')
    numbers = [9, 41, 12, 3, 74, 15]
    numbers.sort(reverse=True)
    for i in numbers:
        print(i)

def smallest():
    print("Smallest to biggest")
    numbers = [9, 41, 12, 3, 74, 15]
    numbers.sort(reverse=False)
    for i in numbers:
        print(i)

biggest()
print("\n")
smallest()
