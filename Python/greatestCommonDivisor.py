#Greatest Common Divisor
import math


#Calculating the gcd of 2 numbers.
x = 86
y = 44
n = min(x,y)


gcd = 0
for i in range(1,n+1):
    if x%i == 0 and y%i == 0:
        gcd = i
        
print(f"The computed GCD of {x} and {y} is {gcd}.")