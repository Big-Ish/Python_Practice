text = ""

while True:
    user_input = input("Enter a 10 letter word: ")
    text = user_input
    if len(user_input) < 10:
        inputted_word = input("Error!, Enter a 10 letter word: ")
    else:
        break

print(":)")
