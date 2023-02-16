rainfall = []
years = int(input("Enter the amount of years: "))

for y in range(1, years+1):
    for m in range(1, 13):
        inches = int(input(f"Enter the inches of rainfall for Year {y}, Month {m}: "))
        rainfall.append(inches)

print("")
print(f"Total months: {len(rainfall)}")
print(f"Total inches of rainfall for {y*m} months: {sum(rainfall)}")
print(f"Average rainfall: {sum(rainfall)/len(rainfall)}")
