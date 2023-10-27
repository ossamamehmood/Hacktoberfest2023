#Password generator
import random

l='abcefghijklmnopqrstuvwxyz'
u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n='1234567890'
sc='!@#$%^&*'
p=''
length=int(input('Enter length of password - '))
while length>0:
    length-=1
    s=random.choice([l,u,n,p])
    p=p+str(random.choice(s))
print(p)
