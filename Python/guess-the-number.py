import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of attempts
attempts = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Thanks for playing!")
