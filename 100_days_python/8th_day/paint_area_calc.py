# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

import math

def paint_calc(h, w, c):
    a = math.ceil((h * w) / c)
    print(f"You'll need {a} cans of paint.")


h = float(input("Height of wall: "))
w = float(input("Width of wall: "))
c = 5

paint_calc(h, w, c)
