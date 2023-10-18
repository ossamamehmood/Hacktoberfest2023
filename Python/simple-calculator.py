print("********** SIMPLE CALCULATOR **********\n")

# Prompting input from the user
firstNumber = input("Enter First Number: ")
a = float(firstNumber)
secondNumber = float(input("Enter Second Number: "))
b = float(secondNumber)

print("\nEnter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for power i.e. (First Number)^(Second Number)")
print("Enter 6 for finding remainder")
print("Enter 7 for integer division\n")

# Prompting operation from the user
operation = int(input("Enter the number here: "))

# Printing the result for operations done by user
print("\nResult:")

if operation == 1:
    print(a + b)
elif operation == 2:
    print(a - b)
elif operation == 3:
    print(a * b)
elif operation == 4:
    print(a / b)
elif operation == 5:
    print(a ** b)
elif operation == 6:
    print(a % b)
elif operation == 7:
    print(a // b)
