import random
def guess_number():
    number = random.randint(0,100)
    score = 100

    while True:
        guess = int(input("Guess the number between 1 to 100: "))


        if guess == number:
            print("Congragulations! You guessed it right " "\n" "Your score is:",score)
            break
        elif guess > number:
            print("Try Again!""\n""HINT: you're number is too high.")
            score -= 10
        else:
            print("Try Again!""\n""HINT: you're number is too less.")
            score -= 10
        if score == 0 :
            print("OOPS! The correct answer is:", number)
            break
guess_number()
