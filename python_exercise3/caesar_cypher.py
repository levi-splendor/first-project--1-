def caesar_encrypt(text, shift):
    result = ""
    # Reduce shift to 0-25 range
    shift = shift % 26
    
    for char in text:
        if char.isupper():  # Uppercase letters
            # Shift within A-Z
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
            
        elif char.islower():  # Lowercase letters
            # Shift within a-z
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
            
        else:
            # Non-letter characters (spaces, punctuation, numbers, etc.)
            result += char  
    return result
def caesar_decrypt(text, shift):
    # Decrypting is just encrypting with negative shift
    return caesar_encrypt(text, -shift)
text = "Hello, World!"
shift = 3

encrypted = caesar_encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)