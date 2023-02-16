fat = float(input("Enter fat grams: "))
carb = float(input("Enter carb grams: "))

def c_f_f(fat):
    calories = fat * 9
    print("Calories from fat: ", calories)

def c_f_c(carb):
    calories = carb * 4
    print("Calories from carb: ", carb)

c_f_c(fat)
c_f_f(carb)