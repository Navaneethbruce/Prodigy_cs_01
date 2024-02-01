def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

# Take input from the user
input_text = input("Enter the text: ")
shift_value = int(input("Enter the shift value: "))

# Encrypt the input text
encrypted_text = caesar_cipher(input_text, shift_value)
print("Encrypted:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = caesar_cipher(encrypted_text, -shift_value)
print("Decrypted:", decrypted_text)