import random


def menu():
    print(
    "\n"
    "__    __                                                                    \n"+
    "|  \  |  \                                                                  \n"+
    "| $$  | $$  ______   _______    ______   ______ ____    ______   _______    \n"+
    "| $$__| $$ |      \ |       \  /      \ |      \    \  |      \ |       \   \n"+
    "| $$    $$  \$$$$$$\| $$$$$$$\|  $$$$$$\| $$$$$$\$$$$\  \$$$$$$\| $$$$$$$\  \n"+
    "| $$$$$$$$ /      $$| $$  | $$| $$  | $$| $$ | $$ | $$ /      $$| $$  | $$  \n"+
    "| $$  | $$|  $$$$$$$| $$  | $$| $$__| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$  \n"+
    "| $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$ | $$ | $$ \$$    $$| $$  | $ $ \n"+
    "\$$   \$$  \$$$$$$$ \$$   \$$ _ \$$$$$$$ \$$  \$$  \$$  \$$$$$$$ \$$   \$$  \n"+
    "                              |  \__| $$                                    \n"+
    "                               \$$    $$                                    \n"+
    "                                \$$$$$$                                     \n"+
    "")


def lose():
    print(
    "\n"
    " __      __                         __                                 \n"+
    "/  \    /  |                       /  |                                \n"+
    " $$  \  /$$/______   __    __      $$ |  ______    _______   ______    \n"+
    " $$  \/$$//      \ /  |   /  |     $$ | /      \  /       | /      \   \n"+
    "  $$  $$//$$$$$$  |$$ |  $$ |      $$ |/$$$$$$  |/$$$$$$$/ /$$$$$$  |  \n"+
    "   $$$$/ $$ |  $$ |$$ |   $$ |     $$ |$$ |  $$ |$$      \ $$    $$ |  \n"+
    "    $$ | $$ \__$$ |$$ \__$$ |      $$ |$$ \__$$ | $$$$$$  |$$$$$$$$/   \n"+
    "    $$ | $$    $$/ $$    $$/       $$ |$$    $$/ /     $$/ $$       |  \n"+
    "    $$/   $$$$$$/   $$$$$$/        $$/  $$$$$$/  $$$$$$$/   $$$$$$$/   \n"+
    "                                                                       \n"+
    "")

def win():
    print(
    "\n"
    "                                                                \n"+
    " /$$     /$$                        /$$      /$$ /$$            \n"+
    "|  $$   /$$/                       | $$  /$ | $$|__/            \n"+
    " \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$   \n"+
    "  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$  \n"+
    "   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$  \n"+
    "    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$  \n"+
    "    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$  \n"+
    "    |__/  \______/  \______/       |__/     \__/|__/|__/  |__/  \n"+
    "                                                                \n"+
    "                                                                \n"+
    "")


def display_f(chosen_word, display):
    #TODO-3: - Create an empty List called display.
    #For each letter in the chosen_word, add a "_" to 'display'.
    #So if the chosen_word was "apple", display should be 
    # ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
    for i in range(len(chosen_word)):
        display.append("_")
    return display


def guesses(chosen_word, guess, display, tries, guessed):
    # TODO-4: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    
    if guess in chosen_word:
        print("\nCorrect!")
        for p in range(len(chosen_word)):
            if chosen_word[p] == guess:
                display[p] = guess
    else:
        tries -= 1
        print(f'\nIncorrect :( You have {tries} tries left.\n')
        
    if guess in chosen_word:
        guessed.append(guess.upper())
    else:
        guessed.append(guess)
        
    print("\n   > Already guessed letters || Caps = correct guesses || \n\n\t", guessed)
    print("\n-------------------------------------------------------------------")
    print("\n",display)
    return tries


def winner(display):
    for i in range (len(display)):
        if "_" not in display:
            return True


def hangman_menu(hangman_pic):
    hangman_pic = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========''', 

    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', 

    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', 

    '''
    +---+
         |
     O   |
    /|   |
         |
         |
    =========''', 

    '''
    +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========''', 

    '''
    +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========''', 

    '''
    +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========='''
    
    ]
    return hangman_pic

def main():
    menu()
    word_list = ["baboon", "camel", "ashik", "nikila,", "ishkanda", "aalok", "conservation", "scandal", "sandal", "randomized", 
                 "parley", "india", "nepal", "astonishing", "vedula", "mishra", "ikea", "pizza", "cococola", "meatballs", "hangman"]
    display = []
    hangman_pic = []
    tries = 7
    guessed = []
    
    # TODO-1 - Randomly choose a word from the word_list 
    # and assign it to a variable called chosen_word.
    
    chosen_word = random.choice(word_list)
    display_f(chosen_word, display)
    
    print(f'Try to guess the word. \nYou have {tries} chances. \nGood Luck!\n')
    #print("\nHint:", chosen_word)
    print("\n",display)
    
    while True:
        # TODO-2 - Ask the user to guess a letter and assign their answer
        # to a variable called guess. Make guess lowercase.
        hangman_pic = hangman_menu(hangman_pic)
        if tries == 6:
            print(hangman_pic[0])
        elif tries == 5:
            print(hangman_pic[1])
        elif tries == 4:
            print(hangman_pic[2])
        elif tries == 3:
            print(hangman_pic[3])
        elif tries == 2:
            print(hangman_pic[4])
        elif tries == 1:
            print(hangman_pic[5])     

        guess = input("\nYour guess: ").lower()
        tries = guesses(chosen_word, guess, display, tries, guessed)
        
        if winner(display) == True:
            win()
            print(f'Congrats on guessing the word! \n\nThe word was || {chosen_word.upper()} ||' )
            print("")
            break
        elif tries == 0:
            print(hangman_pic[6])
            lose()
            print(f'\nPssssh, btw the word was {chosen_word.upper()} ;) ')
            print("")
            break
        else:
            continue


main()