import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password (default is 12): "))
    password = generate_password(length)
    print(f"Generated Password: {password}")
