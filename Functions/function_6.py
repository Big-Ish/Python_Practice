loan = float(input("Enter the monthly cost of Loan Payment: "))
insurance = float(input("Enter the monthly cost of Insurance: "))
gas = float(input("Enter the monthly cost of Gas: "))
oil = float(input("Enter the monthly cost of Oil: "))
tires = float(input("Enter the monthly cost of Tires: "))
maintence = float(input("Enter the monthly cost of Maintence: "))
total_cost = 0

def automobile_cost(loan, insurance, gas, oil, tires, maintence, total_cost):
    total_cost = loan + insurance + gas + oil + tires + maintence
    print("Total cost: ", total_cost)

automobile_cost(loan, insurance, gas, oil, tires, maintence, total_cost)