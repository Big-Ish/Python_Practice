def calc(age):
    span = 90 - age
    day = span*365
    week = span*52
    month = span*12

    print(f'You have {day} days, {week} weeks, and {month} months to live :(')


age = int(input("What is your current age? "))

calc(age)
