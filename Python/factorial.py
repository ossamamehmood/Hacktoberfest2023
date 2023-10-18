import math

# Prompt the user for input
user_input = input("Enter a number to calculate its factorial: ")

try:
    # Convert the input to an integer
    n = int(user_input)
    
    # Calculate the factorial of the input number using math.factorial
    result = math.factorial(n)
    
    # Display the result
    print(f"Factorial of {n} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
