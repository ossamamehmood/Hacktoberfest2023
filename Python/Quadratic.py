# Program to find roots of a Quadratic Equation

import math as m
import cmath as cm
print("For a standard quadratic equation,ax²+bx+c=0,enter the coefficients below")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==0:
    print("Value of a should not be zero")
    print('Please enter a non-zero number')
else:
    dmt=b*b-4*a*c
    if dmt>0:
        r1=(-b+m.sqrt(dmt))/(2*a)
        r2=(-b-m.sqrt(dmt))/(2*a)
        print("We Get Two DISTINCT REAL ROOTS")
        print("1st root is",r1,'&',"2nd root is",r2)
    elif dmt==0:
        r=-b/(2*a)
        print("We Get Two EQUAL REAL ROOTS")
        print("1st and 2nd both roots  are",r)
    else :
        r1=(-b+cm.sqrt(dmt))/(2*a)
        r2=(-b-cm.sqrt(dmt))/(2*a)
        print("We Get Two DISTINCT IMAGINARY ROOTS")
        print("1st root is",r1,'&',"2nd root is",r2)
