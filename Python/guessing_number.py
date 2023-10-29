import random

def subMenu():
    print()
    print("0 - that is my number")
    print("1 - lower than that one")
    print("2 - higher than that one")

def main ():
    print("************************************")
    print("** Guess one number between 1-100 **")
    print("************************************")
    print()
    min = 1
    max = 100
    choice = random. randint(min, max)
    print("Does " + str(choice) + " your number?")
    subMenu()
    answer = int(input(""))
    if answer == 1:
        max = choice
    elif answer == 2:
        min = choice
    while answer != 0:
        if answer == 1:
            newNumber = random.randint(min, max)
        elif answer == 2:
            newNumber = random.randint(min, max)
        print("Does " + str(newNumber) + " your number?")
        subMenu()
        answer = int(input(""))
        if answer == 1:
            max = newNumber - 1
        elif answer == 2:
            min = newNumber + 1
    print()
    print("Leaving program...")
    inp = input("Press any key...")

main()