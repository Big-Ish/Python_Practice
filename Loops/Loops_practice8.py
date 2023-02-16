cond = "y"

while cond == "y":
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    added = num_1+num_2
    print(f'Sum: ', added)
    
    cond = input("Do you want to enter another number? (y/n): ")
    if cond == "y": 
        continue
    else:
        cond == "n"
        break
print("Program terminated")

