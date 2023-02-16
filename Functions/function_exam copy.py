def computepay(hours, payrate_base):
    if hours <= 40:
        grosspay = float(hours)*(payrate_base)
    else:
        grosspay = float(1.5*(hours-40.00)*(payrate_base)+40.00*payrate_base)
    return grosspay


hours = int(input("Enter you work hours: "))
payrate_base = float(input("Enter your payrate: "))

print("Pay: ", computepay(hours, payrate_base))
