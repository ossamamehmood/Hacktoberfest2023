'''
1.  input() function

#single input
user_input = input("Enter something: ")
print(user_input)

#multiple input
user_inputs = [];

while True:
    user_input = input("Enter a msg or press enter to finish : ")

    if not user_input:
        break

    user_inputs.append(user_input)

for i in user_inputs:
    print(i)

'''



'''
2.Command line arguments
import sys

arg1 = []
for i in sys:
    arg1.append(sys.argv)
print(arg1)

# for multiple input we can use argparse
''' 



'''
3. Reading from files:



file_path = "E:\Python files\example.txt"
with open(file_path, "r") as file:
    data = file.read()
print("File data:", data)

'''


'''
4. Standard Input (stdin):

import sys

user_input = sys.stdin.readline()
print(user_input)
'''


'''
5. Working with directories


import os
files = os.listdir('E:/Python files/')
print(files)
print(type(files))
print(files[0])

with open(files[0],'r')as file:
    data = file.read()    
print("File data:", data)

'''

'''
6. Working with External APIs:

import requests
response = requests.get('https://api.example.com/data')
data = response.json()

'''


'''
7.Serialization and Deserialization:

import json
data = {'name': 'John', 'age': 30}
json_data = json.dumps(data)
print(json_data)
'''


'''
8. Database Access:

import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM mytable')

'''