import random

def guess_the_number():
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Higher!")
            elif user_guess > secret_number:
                print("Lower!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

