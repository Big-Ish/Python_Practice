import random

names_string = input("Give me everybody's names, seperated by a comma.\n")

names = names_string.split(", ")
randname = random.randrange(len(names))

print(f'{names[randname]} is going to buy the meal today!')
