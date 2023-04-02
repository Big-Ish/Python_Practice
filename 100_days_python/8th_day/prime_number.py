# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# so no decimals
# if a number can be cleanly divded by anything else than 1 and itself, it is not a prime number.


def prime_checker(n): 
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(n)

