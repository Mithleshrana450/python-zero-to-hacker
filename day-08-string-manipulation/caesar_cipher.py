def caesar_cipher(message, shift, mode):
    result = ""

    # Reverse the shift for decoding
    if mode.lower() == "decode":
        shift = -shift

    for char in message:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Handle lowercase letters
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            # Leave spaces, numbers, and symbols unchanged
            result += char

    return result


# Example usage
message = input("Enter message: ")
shift = int(input("Enter shift value: "))
mode = input("Enter mode (encode/decode): ")

print("Result:", caesar_cipher(message, shift, mode))