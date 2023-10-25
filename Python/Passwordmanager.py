from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
from random import choice,randint,shuffle
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    password_list=password_numbers+password_symbols+password_letters
    shuffle(password_list)
    password = "".join(password_list)
    pasword_entries.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=websit_entries.get()
    email=email_entries.get()
    password=pasword_entries.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS", message="please make sure you haven't left any fields empty .")
    else:
        is_ok=messagebox.askyesno(title=website,message=f"These are the details entered: \nEmail:{email} \n{password} \n is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} / {email}  /{password} \n")
                websit_entries.delete(0, END)
                pasword_entries.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)
canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
website_label.focus()
email_label=Label(text="email/username")
email_label.grid(row=2,column=0)
pasword_label=Label(text="Password")
pasword_label.grid(row=3,column=0)

websit_entries=Entry(width=35)
websit_entries.grid(row=1,column=1,columnspan=2)
email_entries=Entry(width=35)
email_entries.grid(row=2,column=1,columnspan=2)
email_entries.insert(0,"sparshrawat34@gmail.com")
pasword_entries=Entry(width=17)
pasword_entries.grid(row=3,column=1)


generate_password=Button(text="Generate Password",command=generate)
generate_password.grid(row=3,column=2)
add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=5,column=1,columnspan=2)



window.mainloop()
