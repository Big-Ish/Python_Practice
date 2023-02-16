fast_lap = 0
slow_lap = 0
time = []

laps = int(input("Enter the amount of laps: "))

for lap in range(1, laps+1):
    a = float(input(f"Enter the time for lap {lap}: "))
    time.append(a)
while True:
    if fast_lap == 0:
        fast_lap = max(time)
    elif slow_lap == 0:
        slow_lap = min(time)
        break

print(f"\nFastest lap: {fast_lap}")
print(f"Slowest lap: {slow_lap}")
print(f"Average: {sum(time)/len(time)}")