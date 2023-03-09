year = int(input("Enter Year: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Leap year")

elif year % 400 != 0 or year % 4 != 0 and year % 100 == 0:
    print("Not a leap year")
