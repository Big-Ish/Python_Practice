tax = 0
ass = 0

def taxes(property, ass, tax):
    ass = property * 0.6
    tax = (ass * 0.72 / 100)
    print("Assests: ", ass, "kr")
    print("Tax: ", tax, "kr")
    #return ass, tax

property = float(input("Enter property value: "))

print(taxes(property, ass, tax))
#taxes(property)

