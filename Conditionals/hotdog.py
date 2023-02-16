import math

hotdog = 10
buns = 8

people = int(input("Enter the amount attending the cookout: "))
num_of_hotdogs_per_person = int(input("Enter the amount of hotdogs each person will recieve: "))

min_hotdog_package = (people*num_of_hotdogs_per_person)/hotdog
min_buns = (people*num_of_hotdogs_per_person)/buns
print("Minimum hotdog package: ", math.ceil(min_hotdog_package))
print("Minimum buns: ", math.ceil(min_buns))

leftoverhotdog = hotdog-(((people*num_of_hotdogs_per_person))%hotdog)
leftoverbuns = buns-((people*num_of_hotdogs_per_person)%buns)
print(leftoverhotdog)

if leftoverhotdog != 10:
    print(leftoverhotdog)
else:
    print("No hotdogs left!")

if leftoverbuns != 8:
    print(leftoverbuns)
else:
    print("No buns left!")

