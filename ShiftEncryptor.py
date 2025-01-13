def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    
    :param text: The input message as a string.
    :param shift: The integer shift value.
    :param mode: Either 'encrypt' or 'decrypt'.
    :return: The transformed message as a string.
    """
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    result = ''
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine ASCII offset for uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Apply shift and wrap around using modulo
            shifted = (ord(char) - offset + shift) % 26 + offset
            result += chr(shifted)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result


# User interaction
def main():
    print("Caesar Cipher Program")
    mode = input("Do you want to 'encrypt' or 'decrypt' a message? ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter the message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return
    
    result = caesar_cipher(text, shift, mode)
    print(f"Result ({mode}ed): {result}")


if __name__ == "__main__":
    main()
