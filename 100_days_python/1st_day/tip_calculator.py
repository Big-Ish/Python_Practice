bill = int(input("Enter the total bill: €"))
tip = int(input("Enter the tip(%): "))
split = int(input("Enter the amount of people to split the bill with: "))

each_bill = (bill/split) * ((100 + tip)/100)
rounded_bill = round(each_bill, 2)

print(f"Each individual should pay: € {rounded_bill}")
