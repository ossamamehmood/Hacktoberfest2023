import random

word_list = ["python", "programming", "beginner", "hangman"]
word = random.choice(word_list)
guessed_letters = []
attempts = 6

while attempts > 0:
    display_word = "".join([letter if letter in guessed_letters else '_' for letter in word])
    print(display_word)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        if set(word) == set(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts left.")

if attempts == 0:
    print(f"Out of attempts. The word was: {word}")
