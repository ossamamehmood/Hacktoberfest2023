#!/usr/bin/python3
import sys
import os
def enc():
    text=sys.argv[2]
    nameoffile=sys.argv[3]

    word_ord=[]

    secret_null=[]
    file=open(f'{nameoffile}',"w")
    for i in range(len(text)):
	    word_ord.append(ord(text[i]))



    for j in word_ord:
	    secret_null.append("\u200b"*j)

    for i in range(len(secret_null)):
	    file.write(secret_null[i])
	    file.write("\n")
    file.close()
    print('\n\t\t\033[1;32m C - 0 - V - E - R  - T - X \n')
    print("\t\t\033[1;3m  File Saved as : "+str(file.name))



def decoder():
    sec=''
    reader=sys.argv[2]
    encfile=open(reader,'rb')
    num=len(encfile.readlines())
    output=open('decoded.txt','w')
    anotherfile=open(reader,'r')
    for i in range(num):
        sec+=chr(len(anotherfile.readline())-1)
    output.write(sec)
    print(sec)
    output.close()
    anotherfile.close()
    encfile.close()


try:
	if((sys.argv[1]=='-d') and (len(sys.argv)==3)):
		decoder()
	elif ((sys.argv[1]=='-e') and (len(sys.argv)==4)):
		enc()
	else:
		print("Invalid BRO")
except Exception as e:
	print("Invalid Input")





