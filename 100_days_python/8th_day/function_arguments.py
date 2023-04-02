# positional arguments

def greetwith1(location, name):
    print("\ngreet 1")
    print(f"Hello {name}")
    print(f"How is weather in {location}")

greetwith1("Jeff", "Sweden")    # parameters are positional, jeff = location in def(): 


# keyword arguments

def greetwith2(location = "Sweden", name = "Jeff", ):
    print("\ngreet 2")
    print(f"Hello {name}")
    print(f"How is weather in {location}")

greetwith2()    # does not need parameters because it is declared as an argument in def():


# testing positional and keyword arguments
def greetwith3(location, name):
    print("\ngreet 3")
    print(f"Hello {name}")
    print(f"How is weather in {location}")

greetwith3(name = "Jeff", location= "Sweden")
