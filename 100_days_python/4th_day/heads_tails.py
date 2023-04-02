import random

again = input(f"Press '1' to start: ")

while True:
    
    output = random.randint(0, 1)
    if output == 0:
        print("\nHEADS\n")
    else:
        print("\nTAILS\n")
    
    again = input(f"Press '1' to go again: ")
    if again != "1":
        break

print("\nProgram closed\n")
