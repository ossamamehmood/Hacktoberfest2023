def prime_factors(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    return factors

# Input from the user
num = int(input("Enter a number: "))

if num <= 1:
    print("Prime factors are not defined for numbers less than 2.")
else:
    factors = prime_factors(num)
    if len(factors) == 1:
        print(f"{num} is a prime number.")
    else:
        print(f"The prime factors of {num} are: {factors}")
