import math

w = input("Weight: ")
h = input("Height: ")

bmi = int(w) / float(h) ** 2

if bmi >= 18.5 and bmi <= 25:
    print(f"Your BMI is {math.ceil(bmi)}, you're healthy")
elif bmi <= 18.5:
    print(f"Your BMI is {math.ceil(bmi)}, you're underweight")
elif bmi > 25 and bmi < 30:
    print(f"Your BMI is {math.ceil(bmi)}, you're slighty overweight")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {math.ceil(bmi)}, you're obese. Hit the gym :(")
else:
    print(
        f"Your BMI is {math.ceil(bmi)}, Holyy molly, you're clinically obese")
