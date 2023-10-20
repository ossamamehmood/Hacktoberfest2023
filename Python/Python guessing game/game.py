import random

def guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20. Try to guess it.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Try a higher number.")
            elif user_guess > number_to_guess:
                print("Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    guessing_game()

