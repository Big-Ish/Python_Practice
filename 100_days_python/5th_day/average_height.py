heights = []

while True:
    student_heights = int(input("\nEnter student height (cm): "))
    heights.append(student_heights)
    print(f'\nStudent heights: {heights}')
    choice = input("Do you want to add more? (Y/N): ").lower()
    if choice != "y":
        break

total = 0
for h in heights:
    total += h

avg = total / len(heights)
print(f'\nThe total height is: {total} cm.')
print(f'The average height is {round(avg)} cm.')
