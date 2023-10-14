"""
This Python program generates a random number within a user-defined range and lets the player guess the number.
It provides feedback on whether the guess is too high or too low and keeps track of the number of attempts.
The goal is to guess the correct number in as few attempts as possible.
"""

import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between a range you define.")

    # Get the range of numbers from the user
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))

    # Generate a random number within the given range
    secret_number = random.randint(lower_limit, upper_limit)

    # Initialize variables
    attempts = 0
    guess = None

    while guess != secret_number:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
    
    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

if __name__ == "__main__":
    guess_the_number()
