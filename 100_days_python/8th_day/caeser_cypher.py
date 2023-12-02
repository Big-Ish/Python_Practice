def menu():
    
    print(""+
    "\n"
    "\n"
    "   ______                                                       ______                    __                          \n"+
    "  /      \                                                     /      \                  |  \                         \n"+
    " |  $$$$$$\ ______   ______   _______  ______   ______        |  $$$$$$\__    __  ______ | $$____   ______   ______   \n"+
    " | $$   \$$|      \ /      \ /       \/      \ /      \       | $$   \$|  \  |  \/      \| $$    \ /      \ /      \  \n"+
    " | $$       \$$$$$$|  $$$$$$|  $$$$$$|  $$$$$$|  $$$$$$\      | $$     | $$  | $|  $$$$$$| $$$$$$$|  $$$$$$|  $$$$$$\ \n"+
    " | $$   __ /      $| $$    $$\$$    \| $$    $| $$   \$$      | $$   __| $$  | $| $$  | $| $$  | $| $$    $| $$   \$$ \n"+
    " | $$__/  |  $$$$$$| $$$$$$$$_\$$$$$$| $$$$$$$| $$            | $$__/  | $$__/ $| $$__/ $| $$  | $| $$$$$$$| $$       \n"+
    "  \$$    $$\$$    $$\$$     |       $$\$$     | $$             \$$    $$\$$    $| $$    $| $$  | $$\$$     | $$       \n"+
    "   \$$$$$$  \$$$$$$$ \$$$$$$$\$$$$$$$  \$$$$$$$\$$              \$$$$$$ _\$$$$$$| $$$$$$$ \$$   \$$ \$$$$$$$\$$       \n"+
    "                                                                       |  \__| $| $$                                  \n"+
    "                                                                        \$$    $| $$                                  \n"+
    "                                                                         \$$$$$$ \$$                                  \n"+
    "") 


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift, encrypted):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' 
    # forwards in the alphabet by the shift amount and print the encrypted text.
    print(f"\nOriginal Text: {text}")
    for i in text:
        encrypted.append(ord(i)+shift)  # 'ord' converts string to its ascii value and '+shift' adds to the ascii value.)
        
    for i in range (len(encrypted)):
        encrypted[i] = chr(encrypted[i]) # 'chr' converts ascii value back to its str/char value
        
    encrypted_str = "".join(encrypted)
    print(f"\nEncrypted Text: {encrypted_str}")


#TODO-2: Decrypt encryption
def decrypt(text, shift, decrypted):
    print(f"\nOriginal Text: {text}")
    for i in text:
        decrypted.append(ord(i)-shift)
    
    for i in range(len(decrypted)):
        decrypted[i] = chr(decrypted[i])
    
    decrypted_str = "".join(decrypted)
    print(f"\nDecrypted Text: {decrypted_str}")


def stored_cyphers(encrypted):
    print(encrypted)


def main():
    menu()
    while True:
        direction = input("\nPress '1' to Encrypt or Press '2' to Decrypt: and '3' to show ")
        if direction == "1" or direction == "2":
            break
        else:
            print("Invalid input!")
        
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))
    encrypted = []
    decrypted = []
    
    if direction == "1":
        print("\n--------------------------------")
        encrypt(text, shift, encrypted)
        print("\n--------------------------------")
    elif direction == "2":
        print("\n--------------------------------")
        decrypt(text, shift, decrypted)
        print("\n--------------------------------")
    elif direction == "3":
        stored_cyphers(encrypted)


main()