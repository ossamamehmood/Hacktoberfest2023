a = int(input("Enter the lower bound (a): "))
b = int(input("Enter the upper bound (b): "))

# Define a dictionary to map numbers to their English representation
number_words = {
    1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}

for n in range(a, b + 1):
    if 1 <= n <= 9:
        # Print the English representation for numbers 1-9
        print(number_words[n])
    elif n > 9 and n % 2 == 0:
        # Print "even" for even numbers greater than 9
        print("even")
    elif n > 9 and n % 2 == 1:
        # Print "odd" for odd numbers greater than 9
        print("odd")
