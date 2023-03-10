print("\nWelcome to the Love Calculator!\n")

name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e") + name2.count("e")

total1 = t+r+u+e
total2 = l+o+v+e2
final_tot = int(str(total1) + str(total2))

if final_tot < 10 or final_tot > 90:
    print(
        f'Your score is {final_tot}, you go together like coke and mentos.')

elif final_tot >= 40 and final_tot <= 50:
    print(f'Your score is {final_tot}, you are alright together.')

else:
    print(f'Your score is {final_tot}.')
