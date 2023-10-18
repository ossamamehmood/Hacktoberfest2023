def factorial(n):
    if n < 0:
        return "Error"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"The factorial is {factorial(num)}")

