"""Write a Python program to validate email address."""
import re
patt='^[\w\.\-]+@[\w\.\-]+.(com|in|edu)'
txt="harshli-l_patel123@gmail.com"
res=re.search(patt,txt)
print("result",res)