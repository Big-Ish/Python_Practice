# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
#             , 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
#             't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("\nType '1' to encrypt, type '2' to decrypt: ")
text = input("\nType your message: ").lower()
shift = int(input("\nType the shift number: "))
encrypted = []
decrypted = []


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
    print(f"\nEncrypted Text: {encrypted_str}\n")
    return encrypted

#TODO-2: Decrypt encryption
def decrypt(text, shift, decrypted):
    print(f"\nOriginal Text: {text}")
    for i in text:
        decrypted.append(ord(i)-shift)
    
    for i in range(len(decrypted)):
        decrypted[i] = chr(decrypted[i])
    
    decrypted_str = "".join(decrypted)
    print(f"\nDecrypted Text: {decrypted_str}\n")


if direction == "1":
    encrypt(text, shift, encrypted)
elif direction == "2":
    decrypt(text, shift, decrypted)