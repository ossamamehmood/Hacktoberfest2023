import math

def hcf(x,y):
         if x>y:
                  s=y
         else:
                  s=x
         for i in range(1,s+1):
                  if x%i==0 and y%i==0:
                           hcf = i
         return hcf

def lcm(x,y):
         if x > y:  
                  g = x  
         else:  
                  g = y  
         while(True):  
                  if((g % x == 0) and (g % y == 0)):  
                           lcm = g  
                           break  
                  g+= 1  

         return lcm

def factorial(x):
         f = 1
         for i in range(1,x+1):
                  f*=1
         return f

def prime_check(x):
         for i in range(2,(x//2)+1):
                  if x%i==0:
                           print("Not a Prime!")
                  else:
                           print("It is a Prime No!")
                           
def sum():
         sum1 = 0
         while True:
                  a = input("Enter the Numbers-")
                  if a == "":
                           break
                  else:
                           a = int(a)
                           sum1 = a+sum1
         print(sum1)

def mul():
         mul = 0
         while True:
                  a = input("Enter the Numbers/press enter to get result-")
                  if a == "":
                           break
                  else:
                           a = int(a)
                           mul*=a
         print(mul)

def div(x,y):
         return x/y

def power(x,y):
         return (x**y)

def sqroot(x):
         return math.sqrt(x)

def sinA(x):
         return math.sin(x)

def cosA(x):
         return math.cos(x)

def tanA(x):
         return math.tan(x)

def logrithm(x):
         return math.log(x)

def roots():
         while True:
                  x = int(input('Enter a-'))
                  if x != 0:
                           y = int(input('Enter b-'))
                           z = int(input('Enter c-'))

                           import math
                           root1 = -b+math.sqrt(pow(b,2)-(4*a*c))/2*a
                           root2 = -b-math.sqrt(pow(b,2)-(4*a*c))/2*a
                           print(f'Roots are= {root1} and {root2}')
                           break
                  else:
                           print('\'a\' cannot be 0....try again!!!') 


         

