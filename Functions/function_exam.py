def computepay(hours, payrate_base):
    pay = float(1.5*(hours-40.00)*(payrate_base)+40.00*payrate_base)
    return pay

hours = int(input("Enter you work hours: "))
payrate_base = float(input("Enter your payrate: "))

print("Pay: ", computepay(hours, payrate_base))