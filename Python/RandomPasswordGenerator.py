# Python program to generate random password

import random as r
from tkinter import *
from tkinter.ttk import *

def low():
	entry.delete(0, END)
	length = len1.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
	password = ""

	# if strength is low
	if val.get() == 1:
		for i in range(0, length):
			password += r.choice(lower)
		return password

	# if strength is medium
	elif val.get() == 0:
		for i in range(0, length):
			password += r.choice(upper)
		return password

	# if strength is strong
	elif val.get() == 3:
		for i in range(0, length):
			password += r.choice(digits)
		return password
	else:
		print("Please choose an option")
		


def generate():
	password1 = low()
	entry.delete(0,END)
	entry.insert(10, password1)


root = Tk()
val = IntVar()
len1 = IntVar()
root.title("Random Password Generator")
root.configure(bg="#AFEEEE")


style = Style()
style.configure("TLabel", background="#AFEEEE")
style.configure("TRadiobutton",background="#AFEEEE")
style.configure("TButton",background="#FFC107",foreground="#FFC107")


Random_password = Label(root, text="Password", style="TLabel")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)


c_label = Label(root, text="Length", style="TLabel")
c_label.grid(row=1)


combo = Combobox(root, textvariable=len1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15,
                   16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
		   26, 27, 28, 29, 30, 31, 32, "Length")


combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)


radio_low = Radiobutton(root, text="Low", variable=val, value=1, style="TRadiobutton").grid(row=3,column=0,sticky='W',padx=35)
radio_middle = Radiobutton(root, text="Medium", variable=val, value=0, style="TRadiobutton").grid(row=3,column=1,sticky='W',padx=35)
radio_strong = Radiobutton(root, text="Strong", variable=val, value=3,style="TRadiobutton").grid(row=3,column=2,sticky='W',padx=30)
generate_button = Button(root, text="Generate", command=generate, style="TButton")
generate_button.grid(row=4,column=1, padx=10,pady=10)

root.mainloop()
