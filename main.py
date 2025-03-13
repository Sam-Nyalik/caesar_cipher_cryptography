# Encrpyts input text using Caesar cipher
def caeser_encrypt(text, shift):
    
    # Parameter text - The input string to encrpyt
    # Parameter shift - Integer value which indicates the number of positions each letter of text has been moved down
    
    result = ""
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += encrypted_char
        
        else:
            # Non alphabetic character
            result += char
            
    return result

# Decrypt the input using Caesar cipher
def caesar_decrypt(text, shift):
    
    # Parameter text - The input text to decrypt
    # Parameter shift - Integer value which indicates the number of positions each letter of text has been moved down
    
    return caeser_encrypt(text, -shift)
 
if __name__ == "__main__":
    #  Input message and shift
    message = input("Enter any message: \n")
    shift_value = 3
    
    # Encrypt the message
    encrypted_message = caeser_encrypt(message, shift_value)
    print("Encrypted Message:", encrypted_message)
    
    # Decrypt the message
    decrypted_message = caesar_decrypt(encrypted_message, shift_value)
    print("Decrypted Message:", decrypted_message)