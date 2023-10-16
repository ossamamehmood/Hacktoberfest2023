
# import modules
import string
import random
 
 
# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

ls = []
ls.extend(s1)
ls.extend(s2)
ls.extend(s3)
ls.extend(s4)

# length of password by user
password_length = int(input("---------------enter length of password------------\n"))

password = ""                  # password var declaration
for i in range(password_length):
    ch = random.choice(ls)
    password += ch
    
print(password)
