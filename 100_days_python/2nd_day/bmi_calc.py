import math

h = input("\nHeight (m): ")
w = input("\nWeight (kg): ")

bmi = int(w) / float(h) ** 2

if bmi >= 18.5 and bmi <= 25:
    print(f"\nYour BMI is {math.ceil(bmi)}, You're healthy!")
elif bmi <= 18.5:
    print(f"\nYour BMI is {math.ceil(bmi)}, You're underweight. Ever heard of this thing called a pizza?")
elif bmi > 25 and bmi < 30:
    print(f"\nYour BMI is {math.ceil(bmi)}, You're slighty overweight.")
elif bmi > 30 and bmi < 35:
    print(f"\nYour BMI is {math.ceil(bmi)}, You're obese. Hit the gym.")
else:
    print(
        f"\nYour BMI is {math.ceil(bmi)}, Bruh, you're clinically obese...")
