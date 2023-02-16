import random

opt = [1,2,3]
cpu = random.choice(opt)

def cpuchoice():
    if cpu == 1:
        print("Computer chose: Rock")
    elif cpu == 2:
        print("Computer chose: Paper")
    elif cpu == 3:
        print("Computer chose: Scissors")

def userchoice(usr_choice):
    if usr_choice == 1:
        print("User chose: Rock")
    elif usr_choice == 2:
        print("User chose: Paper")
    elif usr_choice == 3:
        print("User chose: Scissors")

def winner(usr_choice):
    if cpu == usr_choice:
        print("Tie!")
    elif cpu == 1 and usr_choice == 3:
        print("Computer wins!")
    elif cpu == 2 and usr_choice == 1:
        print("Computer wins!")
    elif cpu == 3 and usr_choice == 2:
        print("Computer wins!")
    else:
        print("User wins!")

def main():
    while True:
        try:
            usr_choice = int(input("\nEnter '1' for Rock, '2' for Paper or '3' for Scissors: "))
            if usr_choice >= 4 or usr_choice <= 0:
                print("You think you're smart, eh? Try again ;)")
                continue
            else:
                print("")
                cpuchoice()
                userchoice(usr_choice)
                print("")
                winner(usr_choice)
                again = input(("\nWould you like to play again? ('y' for yes): "))
                if again.lower() == "y":
                    continue
                else:
                    print("Program closed!")
                    break
                
        except ValueError:
            print("Input must be an Integer!")
main()