largest = None
smallest = None
saved_string = []
saved_numbers = []

while True:
    numbers = input("Enter a number: ")
    saved_string.append(numbers)

    if numbers == "done":
        break
    else:
        for i in saved_string:
            saved_numbers = [eval(i) for i in saved_string]
        print(saved_numbers)

saved_numbers.sort(reverse=True)
largest = saved_numbers[0]
print ("Maximum:", largest)

saved_numbers.sort(reverse=False)
smallest = saved_numbers[0]
print ("Smallest:", smallest)

