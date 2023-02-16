speed = int(input("What is the speed of the vehicle in mph?: "))
time = int(input("How many hours has it traveled?: "))
print("")

print("Hours\t\tDistance Traveled")
print("-------------------------------")
for t in range(1, time+1):
    distance = speed * 1
    #print(f'Hour {t}: \tDistance: {distance*t} miles')
    print(f'{t}\t\t{distance*t}')