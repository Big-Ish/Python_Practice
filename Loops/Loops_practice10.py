total_bugs = 0

for i in range(1, 6):
    bugs = int(input(f"Enter the amounts of bugs caught for day {i}: "))
    total_bugs = total_bugs + bugs

print(f"Total bugs collected for 5 days: {total_bugs}")
