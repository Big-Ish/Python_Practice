scores = []

while True:
    student_scores = int(input("\nEnter student score: "))
    scores.append(student_scores)
    print(f'High score: {scores}')

    choice = (input("\nWould like to add more scores? (Y/N): ")).lower()
    if choice != "y":
        break

high_score = 0
for i in scores:
    if i > high_score:
        high_score = i

print(f'\nThe highest score in the class is {high_score}')
