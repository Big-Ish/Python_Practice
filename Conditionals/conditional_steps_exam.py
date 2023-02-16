hours = int(input("Enter you work hours: "))
payrate_base = float(input("Enter your payrate: "))


if hours <= 40:
    grosspay = print ("Your gross pay is", float(hours)*(payrate_base), " DKK")
else:
    grosspay = print ("Your gross pay is", float(1.5*(hours-40.00)*(payrate_base)+
                                                40.00*payrate_base), " DKK")

print (grosspay)