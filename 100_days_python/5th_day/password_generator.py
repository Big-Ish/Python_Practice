import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def main():
    print("\nWelcome to the password generator!")
    while True:
        num_letters = int(input("\nHow many letters do you want?: "))
        num_numbers = int(input("How many numbers do you want?: "))
        num_symbols = int(input("How many symbols do you want?: "))

        password = []

        for l in range(1, num_letters+1):
            password.append(random.choice(letters))

        for n in range(1, num_numbers+1):
            password.append(random.choice(numbers))

        for s in range(1, num_symbols+1):
            password.append(random.choice(symbols))

        # Shuffles the password so it's not in order.
        string_pass = "".join(random.sample(password, len(password)))

        print(f'\nYour random password is: {string_pass}')

        choice = input(
            "\nWould you like to generate another password? ('y' for yes): ").lower()
        if choice != "y":
            print("Program has shut down.")
            break
        else:
            continue


main()
