# Hi, this code is written by Purna Shrestha.
import random
import time
from colorama import Fore, Style
# Please install colorama to enable colorful output. You can install it with 
# 'pip install colorama' command on the terminal.

# Additional prompts
prompts = [
    "Hi, this code is written by Purna Shrestha.",
    "The quick brown fox jumps over the lazy dog",
    "Python is a versatile and powerful programming language",
    "Coding is a skill that can change your life",
    "Practice makes perfect",
    "All for one, and one for all.",
    "The only limit is your imagination.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
]

def display_prompt(prompt):
    print("Type this: ", prompt, "")
    input("Press ENTER when you are ready!")

def calculate_typing_speed(prompt, start_time, end_time):
    words = len(prompt.split())
    elapsed_time = end_time - start_time
    speed = words / (elapsed_time / 60)
    return speed

def play_typing_game():
    prompt = random.choice(prompts)
    display_prompt(prompt)

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    if user_input == prompt:
        print(Fore.GREEN + "Congratulations! You typed it correctly.")
        print(Style.RESET_ALL)  # Reset colorama settings
    else:
        print(Fore.RED + "Sorry, there were errors in your typing:")
        for i in range(len(prompt)):
            if user_input[i:i+1] == prompt[i:i+1]:
                print(Fore.GREEN + user_input[i:i+1], end='')
            else:
                print(Fore.RED + user_input[i:i+1], end='')
        print(Style.RESET_ALL)  # Reset colorama settings

    typing_speed = calculate_typing_speed(prompt, start_time, end_time)
    print("Your typing speed: {:.2f} words/minute".format(typing_speed))

if __name__ == "__main__":
    while True:
        play_typing_game()
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
