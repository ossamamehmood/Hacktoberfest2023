import math
def factorial():
    while True:
        n=int(input("Enter a Non-Negative Number: "))
        print("Factorial of",n,"is",math.factorial(n))
        print("Would You Like to know Factorial of any Other Number ?")
        ch = input("Press (y/n)")
        if ch == "n" or ch == "N":
            print("Thank You For Using")
            break
        else:
            continue
factorial()
