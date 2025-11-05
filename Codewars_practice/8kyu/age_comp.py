import random

dad_years_old = random.randint(40,80)
son_years_old = random.randint(20,40)

def twice_as_old(dad_years_old, son_years_old):
    diff = dad_years_old - (son_years_old * 2)
    return(abs(diff))

print("Dad:", dad_years_old)
print("Son:", son_years_old)
print("Difference:",(twice_as_old(dad_years_old, son_years_old)))