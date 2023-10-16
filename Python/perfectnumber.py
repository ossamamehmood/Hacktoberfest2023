"""
A perfect number is a positive integer that is equal to the sum of its proper
divisors (excluding itself).
For example, 28 is a perfect number because its divisors
(excluding itself) are 1, 2, 4, 7, and 14, and 1 + 2 + 4 + 7 + 14 = 28.
"""


def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number


# Input a number to check if it's a perfect number
num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
