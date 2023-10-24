import string
import random

def generate_password(length, use_digits=True, use_special_chars=True):
    # Define character sets based on complexity requirements
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    # Check for valid length
    if length < 1:
        return "Password length must be at least 1."

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_digits = input("Use digits (y/n): ").lower() == "y"
    use_special_chars = input("Use special characters (y/n): ").lower() == "y"

    password = generate_password(length, use_digits, use_special_chars)
    print("Generated Password:", password)