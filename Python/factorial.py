#Python

# Define a recursive function to calculate the factorial
def factorial(n):
    # Base case: If n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: For n > 1, calculate factorial using recursion
    else:
        # The factorial of n is n multiplied by the factorial of (n-1)
        return n * factorial(n - 1)

# Ask the user for input
number = int(input("Enter a non-negative integer: "))

# Call the factorial function and print the result
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
