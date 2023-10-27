
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as mbox
import tkinter as tk

# created a main window
root = Tk()
root.title("Odd Symbol Find Game")
root.geometry('1000x700')

ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
ans5 = 0

# ------------------------------------- for frame1 -----------------------------------------
class Level1_keypad(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # created each button in form of matrices
        x = tk.Button(self, text=' 😑 ', command=self.board100, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=0, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board101, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=4, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board102, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=8, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board103, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=12, columnspan='4', sticky='news')
        #------
        x = tk.Button(self, text=' 😑 ', command=self.board104, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=16, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board110, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=0, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board111, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=4, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board112, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=8, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board113, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=12, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😐 ', command=self.board114, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=16, columnspan='4', sticky='news')
        #----
        x = tk.Button(self, text=' 😑 ', command=self.board120, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=0, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board121, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=4, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board122, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=8, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board123, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=12, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board124, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=16, columnspan='4', sticky='news')
        #-----
        x = tk.Button(self, text=' 😑 ', command=self.board130, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=0, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board131, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=4, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board132, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=8, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board133, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=12, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board134, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=16, columnspan='4', sticky='news')
        #-----
        x = tk.Button(self, text=' 😑 ', command=self.board140, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=0, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board141, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=4, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board142, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=8, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board143, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=12, columnspan='4', sticky='news')

        x = tk.Button(self, text=' 😑 ', command=self.board144, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=16, columnspan='4', sticky='news')

    def show(self, entry):
        self.target = entry
        self.place(relx=0.3, rely=0.4, anchor='c')
    # created function for eah button
    def board100(self):
        ans0 = Label(f1, text='(0 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board101(self):
        ans0 = Label(f1, text='(0 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board102(self):
        ans0 = Label(f1, text='(0 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board103(self):
        ans0 = Label(f1, text='(0 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board104(self):
        ans0 = Label(f1, text='(0 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board110(self):
        ans0 = Label(f1, text='(1 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board111(self):
        ans0 = Label(f1, text='(1 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board112(self):
        ans0 = Label(f1, text='(1 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board113(self):
        ans0 = Label(f1, text='(1 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board114(self):
        global ans1
        ans1 = 1
        ans0 = Label(f1, text='(1 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board120(self):
        ans0 = Label(f1, text='(2 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board121(self):
        ans0 = Label(f1, text='(2 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board122(self):
        ans0 = Label(f1, text='(2 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board123(self):
        ans0 = Label(f1, text='(2 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board124(self):
        ans0 = Label(f1, text='(2 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board130(self):
        ans0 = Label(f1, text='(3 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board131(self):
        ans0 = Label(f1, text='(3 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board132(self):
        ans0 = Label(f1, text='(3 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board133(self):
        ans0 = Label(f1, text='(3 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board134(self):
        ans0 = Label(f1, text='(3 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board140(self):
        ans0 = Label(f1, text='(4 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board141(self):
        ans0 = Label(f1, text='(4 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board142(self):
        ans0 = Label(f1, text='(4 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board143(self):
        ans0 = Label(f1, text='(4 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board144(self):
        ans0 = Label(f1, text='(4 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
#-------------------------------------------------------

# ------------------------------------- for frame2 -----------------------------------------
# class Keypad created for creating keyboard
class Level2_keypad(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        x = tk.Button(self, text=' 👩 ', command=self.board100, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board101, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board102, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board103, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=9, columnspan='3', sticky='news')
        #------
        x = tk.Button(self, text=' 👩 ', command=self.board104, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=0, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board105, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board110, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board111, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board112, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board113, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board114, font=("Arial", 20), bg="light green", fg="blue",borderwidth=3, relief="raised")
        x.grid(row=1, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board115, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=15, columnspan='3', sticky='news')
        #----
        x = tk.Button(self, text=' 👩 ', command=self.board120, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board121, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board122, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board123, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board124, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board125, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=15, columnspan='3', sticky='news')

        #-----
        x = tk.Button(self, text=' 👩 ', command=self.board130, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board131, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board132, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board133, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board134, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board135, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=15, columnspan='3', sticky='news')
        #-----
        x = tk.Button(self, text=' 👩 ', command=self.board140, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board141, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board142, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board143, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👧🏽 ', command=self.board144, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board145, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board150, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board151, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board152, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board153, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board154, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 👩 ', command=self.board155, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=15, columnspan='3', sticky='news')

    def show(self, entry):
        self.target = entry
        self.place(relx=0.3, rely=0.4, anchor='c')
    def board100(self):
        ans0 = Label(f2, text='(0 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board101(self):
        ans0 = Label(f2, text='(0 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board102(self):
        ans0 = Label(f2, text='(0 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board103(self):
        ans0 = Label(f2, text='(0 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board104(self):
        ans0 = Label(f2, text='(0 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board105(self):
        ans0 = Label(f2, text='(0 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board110(self):
        ans0 = Label(f2, text='(1 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board111(self):
        ans0 = Label(f2, text='(1 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board112(self):
        ans0 = Label(f2, text='(1 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board113(self):
        ans0 = Label(f2, text='(1 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board114(self):
        ans0 = Label(f2, text='(1 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board115(self):
        ans0 = Label(f2, text='(1 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board120(self):
        ans0 = Label(f2, text='(2 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board121(self):
        ans0 = Label(f2, text='(2 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board122(self):
        ans0 = Label(f2, text='(2 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board123(self):
        ans0 = Label(f2, text='(2 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board124(self):
        ans0 = Label(f2, text='(2 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board125(self):
        ans0 = Label(f2, text='(2 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board130(self):
        ans0 = Label(f2, text='(3 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board131(self):
        ans0 = Label(f2, text='(3 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board132(self):
        ans0 = Label(f2, text='(3 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board133(self):
        ans0 = Label(f2, text='(3 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board134(self):
        ans0 = Label(f2, text='(3 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board135(self):
        ans0 = Label(f2, text='(3 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board140(self):
        ans0 = Label(f2, text='(4 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board141(self):
        ans0 = Label(f2, text='(4 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board142(self):
        ans0 = Label(f2, text='(4 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board143(self):
        ans0 = Label(f2, text='(4 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board144(self):
        global ans2
        ans2 = 1
        ans0 = Label(f2, text='(4 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board145(self):
        ans0 = Label(f2, text='(4 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board150(self):
        ans0 = Label(f2, text='(5 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board151(self):
        ans0 = Label(f2, text='(5 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board152(self):
        ans0 = Label(f2, text='(5 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board153(self):
        ans0 = Label(f2, text='(5 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board154(self):
        ans0 = Label(f2, text='(5 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    def board155(self):
        ans0 = Label(f2, text='(5 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    #-------

#-------------------------------------------------------

# ------------------------------------- for frame3 -----------------------------------------
# class Keypad created for creating keyboard
class Level3_keypad(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        x = tk.Button(self, text=' ⌛ ', command=self.board100, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board101, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board102, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board103, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=9, columnspan='3', sticky='news')
        # ------
        x = tk.Button(self, text=' ⌛ ', command=self.board104, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board105, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board106, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board110, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board111, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board112, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board113, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board114, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board115, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⏳ ', command=self.board116, font=("Arial", 13), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=18, columnspan='3', sticky='news')
        # ----
        x = tk.Button(self, text=' ⌛ ', command=self.board120, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board121, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board122, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board123, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board124, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board125, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board126, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=18, columnspan='3', sticky='news')
        # -----
        x = tk.Button(self, text=' ⌛ ', command=self.board130, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board131, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board132, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board133, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board134, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board135, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board136, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=18, columnspan='3', sticky='news')
        # -----
        x = tk.Button(self, text=' ⌛ ', command=self.board140, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board141, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board142, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board143, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board144, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board145, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board146, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board150, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board151, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board152, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board153, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board154, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board155, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board156, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board160, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board161, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board162, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board163, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board164, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board165, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' ⌛ ', command=self.board166, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=18, columnspan='3', sticky='news')

    def show(self, entry):
        self.target = entry
        self.place(relx=0.32, rely=0.4, anchor='c')

    def board100(self):
        ans0 = Label(f3, text='(0 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board101(self):
        ans0 = Label(f3, text='(0 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board102(self):
        ans0 = Label(f3, text='(0 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board103(self):
        ans0 = Label(f3, text='(0 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board104(self):
        ans0 = Label(f3, text='(0 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board105(self):
        ans0 = Label(f3, text='(0 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board106(self):
        ans0 = Label(f3, text='(0 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board110(self):
        ans0 = Label(f3, text='(1 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board111(self):
        ans0 = Label(f3, text='(1 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board112(self):
        ans0 = Label(f3, text='(1 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board113(self):
        ans0 = Label(f3, text='(1 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board114(self):
        ans0 = Label(f3, text='(1 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board115(self):
        ans0 = Label(f3, text='(1 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board116(self):
        global ans3
        ans3 = 1
        ans0 = Label(f3, text='(1 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board120(self):
        ans0 = Label(f3, text='(2 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board121(self):
        ans0 = Label(f3, text='(2 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board122(self):
        ans0 = Label(f3, text='(2 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board123(self):
        ans0 = Label(f3, text='(2 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board124(self):
        ans0 = Label(f3, text='(2 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board125(self):
        ans0 = Label(f3, text='(2 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board126(self):
        ans0 = Label(f3, text='(2 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board130(self):
        ans0 = Label(f3, text='(3 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board131(self):
        ans0 = Label(f3, text='(3 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board132(self):
        ans0 = Label(f3, text='(3 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board133(self):
        ans0 = Label(f3, text='(3 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board134(self):
        ans0 = Label(f3, text='(3 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board135(self):
        ans0 = Label(f3, text='(3 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board136(self):
        ans0 = Label(f3, text='(3 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board140(self):
        ans0 = Label(f3, text='(4 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board141(self):
        ans0 = Label(f3, text='(4 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board142(self):
        ans0 = Label(f3, text='(4 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board143(self):
        ans0 = Label(f3, text='(4 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board144(self):
        ans0 = Label(f3, text='(4 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board145(self):
        ans0 = Label(f3, text='(4 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board146(self):
        ans0 = Label(f3, text='(4 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board150(self):
        ans0 = Label(f3, text='(5 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board151(self):
        ans0 = Label(f3, text='(5 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board152(self):
        ans0 = Label(f3, text='(5 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board153(self):
        ans0 = Label(f3, text='(5 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board154(self):
        ans0 = Label(f3, text='(5 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board155(self):
        ans0 = Label(f3, text='(5 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board156(self):
        ans0 = Label(f3, text='(5 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board160(self):
        ans0 = Label(f3, text='(6 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board161(self):
        ans0 = Label(f3, text='(6 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board162(self):
        ans0 = Label(f3, text='(6 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board163(self):
        ans0 = Label(f3, text='(6 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board164(self):
        ans0 = Label(f3, text='(6 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board165(self):
        ans0 = Label(f3, text='(6 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board166(self):
        ans0 = Label(f3, text='(6 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    #-------

#-------------------------------------------------------

# ------------------------------------- for frame4 -----------------------------------------
# class Keypad created for creating keyboard
class Level4_keypad(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        x = tk.Button(self, text=' 🌏 ', command=self.board100, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board101, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board102, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board103, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=9, columnspan='3', sticky='news')
        # ------
        x = tk.Button(self, text=' 🌏 ', command=self.board104, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board105, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board106, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board107, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board110, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board111, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board112, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board113, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board114, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board115, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board116, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board117, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=21, columnspan='3', sticky='news')
        # ----
        x = tk.Button(self, text=' 🌏 ', command=self.board120, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board121, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board122, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board123, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board124, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board125, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board126, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board127, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=21, columnspan='3', sticky='news')
        # -----
        x = tk.Button(self, text=' 🌏 ', command=self.board130, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board131, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board132, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board133, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board134, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board135, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board136, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board137, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=21, columnspan='3', sticky='news')
        # -----
        x = tk.Button(self, text=' 🌏 ', command=self.board140, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board141, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board142, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board143, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board144, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board145, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board146, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board147, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board150, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board151, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board152, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌎 ', command=self.board153, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board154, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board155, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board156, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board157, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board160, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board161, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board162, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board163, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board164, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board165, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board166, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board167, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board170, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board171, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board172, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board173, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board174, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board175, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board176, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🌏 ', command=self.board177, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=21, columnspan='3', sticky='news')

    def show(self, entry):
        self.target = entry
        self.place(relx=0.35, rely=0.4, anchor='c')

    def board100(self):
        ans0 = Label(f4, text='(0 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board101(self):
        ans0 = Label(f4, text='(0 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board102(self):
        ans0 = Label(f4, text='(0 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board103(self):
        ans0 = Label(f4, text='(0 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board104(self):
        ans0 = Label(f4, text='(0 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board105(self):
        ans0 = Label(f4, text='(0 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board106(self):
        ans0 = Label(f4, text='(0 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board107(self):
        ans0 = Label(f4, text='(0 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board110(self):
        ans0 = Label(f4, text='(1 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board111(self):
        ans0 = Label(f4, text='(1 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board112(self):
        ans0 = Label(f4, text='(1 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board113(self):
        ans0 = Label(f4, text='(1 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board114(self):
        ans0 = Label(f4, text='(1 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board115(self):
        ans0 = Label(f4, text='(1 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board116(self):
        ans0 = Label(f4, text='(1 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board117(self):
        ans0 = Label(f4, text='(1 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board120(self):
        ans0 = Label(f4, text='(2 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board121(self):
        ans0 = Label(f4, text='(2 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board122(self):
        ans0 = Label(f4, text='(2 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board123(self):
        ans0 = Label(f4, text='(2 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board124(self):
        ans0 = Label(f4, text='(2 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board125(self):
        ans0 = Label(f4, text='(2 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board126(self):
        ans0 = Label(f4, text='(2 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board127(self):
        ans0 = Label(f4, text='(2 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board130(self):
        ans0 = Label(f4, text='(3 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board131(self):
        ans0 = Label(f4, text='(3 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board132(self):
        ans0 = Label(f4, text='(3 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board133(self):
        ans0 = Label(f4, text='(3 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board134(self):
        ans0 = Label(f4, text='(3 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board135(self):
        ans0 = Label(f4, text='(3 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board136(self):
        ans0 = Label(f4, text='(3 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board137(self):
        ans0 = Label(f4, text='(3 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board140(self):
        ans0 = Label(f4, text='(4 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board141(self):
        ans0 = Label(f4, text='(4 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board142(self):
        ans0 = Label(f4, text='(4 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board143(self):
        ans0 = Label(f4, text='(4 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board144(self):
        ans0 = Label(f4, text='(4 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board145(self):
        ans0 = Label(f4, text='(4 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board146(self):
        ans0 = Label(f4, text='(4 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board147(self):
        ans0 = Label(f4, text='(4 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board150(self):
        ans0 = Label(f4, text='(5 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board151(self):
        ans0 = Label(f4, text='(5 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board152(self):
        ans0 = Label(f4, text='(5 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board153(self):
        global ans4
        ans4 = 1
        ans0 = Label(f4, text='(5 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board154(self):
        ans0 = Label(f4, text='(5 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board155(self):
        ans0 = Label(f4, text='(5 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board156(self):
        ans0 = Label(f4, text='(5 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board157(self):
        ans0 = Label(f4, text='(5 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board160(self):
        ans0 = Label(f4, text='(6 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board161(self):
        ans0 = Label(f4, text='(6 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board162(self):
        ans0 = Label(f4, text='(6 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board163(self):
        ans0 = Label(f4, text='(6 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board164(self):
        ans0 = Label(f4, text='(6 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board165(self):
        ans0 = Label(f4, text='(6 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board166(self):
        ans0 = Label(f4, text='(6 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board167(self):
        ans0 = Label(f4, text='(6 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board170(self):
        ans0 = Label(f4, text='(7 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board171(self):
        ans0 = Label(f4, text='(7 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board172(self):
        ans0 = Label(f4, text='(7 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board173(self):
        ans0 = Label(f4, text='(7 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board174(self):
        ans0 = Label(f4, text='(7 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board175(self):
        ans0 = Label(f4, text='(7 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board176(self):
        ans0 = Label(f4, text='(7 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board177(self):
        ans0 = Label(f4, text='(7 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    #-------

#-------------------------------------------------------

# ------------------------------------- for frame5 -----------------------------------------
# class Keypad created for creating keyboard
class Level5_keypad(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        x = tk.Button(self, text=' 🕒 ', command=self.board100, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board101, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board102, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board103, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=9, columnspan='3', sticky='news')
        # ------
        x = tk.Button(self, text=' 🕒 ', command=self.board104, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board105, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board106, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board107, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board108, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=0, column=24, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board110, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board111, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board112, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board113, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board114, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board115, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board116, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board117, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board118, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=1, column=24, columnspan='3', sticky='news')
        # ----
        x = tk.Button(self, text=' 🕒 ', command=self.board120, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board121, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board122, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board123, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board124, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board125, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board126, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board127, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board128, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=2, column=24, columnspan='3', sticky='news')
        # -----
        x = tk.Button(self, text=' 🕒 ', command=self.board130, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board131, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board132, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board133, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board134, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board135, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board136, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board137, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board138, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=3, column=24, columnspan='3', sticky='news')
        # -----
        x = tk.Button(self, text=' 🕒 ', command=self.board140, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board141, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board142, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board143, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board144, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board145, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board146, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board147, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board148, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=4, column=24, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board150, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board151, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board152, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board153, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board154, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board155, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕐 ', command=self.board156, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board157, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board158, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=5, column=24, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board160, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board161, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board162, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board163, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board164, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board165, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board166, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board167, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board168, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=6, column=24, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board170, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board171, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board172, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board173, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board174, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board175, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board176, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board177, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board178, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=7, column=24, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board180, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=0, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board181, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=3, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board182, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=6, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board183, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=9, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board184, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=12, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board185, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=15, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board186, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=18, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board187, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=21, columnspan='3', sticky='news')

        x = tk.Button(self, text=' 🕒 ', command=self.board188, font=("Arial", 20), bg="light green", fg="blue",
                      borderwidth=3, relief="raised")
        x.grid(row=8, column=24, columnspan='3', sticky='news')

    def show(self, entry):
        self.target = entry
        self.place(relx=0.35, rely=0.4, anchor='c')

    def board100(self):
        ans0 = Label(f5, text='(0 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board101(self):
        ans0 = Label(f5, text='(0 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board102(self):
        ans0 = Label(f5, text='(0 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board103(self):
        ans0 = Label(f5, text='(0 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board104(self):
        ans0 = Label(f5, text='(0 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board105(self):
        ans0 = Label(f5, text='(0 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board106(self):
        ans0 = Label(f5, text='(0 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board107(self):
        ans0 = Label(f5, text='(0 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board108(self):
        ans0 = Label(f5, text='(0 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board110(self):
        ans0 = Label(f5, text='(1 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board111(self):
        ans0 = Label(f5, text='(1 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board112(self):
        ans0 = Label(f5, text='(1 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board113(self):
        ans0 = Label(f5, text='(1 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board114(self):
        ans0 = Label(f5, text='(1 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board115(self):
        ans0 = Label(f5, text='(1 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board116(self):
        ans0 = Label(f5, text='(1 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board117(self):
        ans0 = Label(f5, text='(1 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board118(self):
        ans0 = Label(f5, text='(1 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board120(self):
        ans0 = Label(f5, text='(2 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board121(self):
        ans0 = Label(f5, text='(2 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board122(self):
        ans0 = Label(f5, text='(2 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board123(self):
        ans0 = Label(f5, text='(2 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board124(self):
        ans0 = Label(f5, text='(2 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board125(self):
        ans0 = Label(f5, text='(2 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board126(self):
        ans0 = Label(f5, text='(2 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board127(self):
        ans0 = Label(f5, text='(2 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board128(self):
        ans0 = Label(f5, text='(2 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board130(self):
        ans0 = Label(f5, text='(3 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board131(self):
        ans0 = Label(f5, text='(3 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board132(self):
        ans0 = Label(f5, text='(3 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board133(self):
        ans0 = Label(f5, text='(3 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board134(self):
        ans0 = Label(f5, text='(3 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board135(self):
        ans0 = Label(f5, text='(3 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board136(self):
        ans0 = Label(f5, text='(3 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board137(self):
        ans0 = Label(f5, text='(3 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board138(self):
        ans0 = Label(f5, text='(3 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board140(self):
        ans0 = Label(f5, text='(4 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board141(self):
        ans0 = Label(f5, text='(4 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board142(self):
        ans0 = Label(f5, text='(4 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board143(self):
        ans0 = Label(f5, text='(4 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board144(self):
        ans0 = Label(f5, text='(4 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board145(self):
        ans0 = Label(f5, text='(4 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board146(self):
        ans0 = Label(f5, text='(4 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board147(self):
        ans0 = Label(f5, text='(4 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board148(self):
        ans0 = Label(f5, text='(4 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board150(self):
        ans0 = Label(f5, text='(5 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board151(self):
        ans0 = Label(f5, text='(5 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board152(self):
        ans0 = Label(f5, text='(5 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board153(self):
        ans0 = Label(f5, text='(5 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board154(self):
        ans0 = Label(f5, text='(5 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board155(self):
        ans0 = Label(f5, text='(5 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board156(self):
        global ans5
        ans5 = 1
        ans0 = Label(f5, text='(5 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board157(self):
        ans0 = Label(f5, text='(5 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board158(self):
        ans0 = Label(f5, text='(5 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board160(self):
        ans0 = Label(f5, text='(6 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board161(self):
        ans0 = Label(f5, text='(6 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board162(self):
        ans0 = Label(f5, text='(6 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board163(self):
        ans0 = Label(f5, text='(6 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board164(self):
        ans0 = Label(f5, text='(6 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board165(self):
        ans0 = Label(f5, text='(6 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board166(self):
        ans0 = Label(f5, text='(6 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board167(self):
        ans0 = Label(f5, text='(6 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board168(self):
        ans0 = Label(f5, text='(6 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board170(self):
        ans0 = Label(f5, text='(7 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board171(self):
        ans0 = Label(f5, text='(7 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board172(self):
        ans0 = Label(f5, text='(7 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board173(self):
        ans0 = Label(f5, text='(7 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board174(self):
        ans0 = Label(f5, text='(7 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board175(self):
        ans0 = Label(f5, text='(7 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board176(self):
        ans0 = Label(f5, text='(7 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board177(self):
        ans0 = Label(f5, text='(7 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board178(self):
        ans0 = Label(f5, text='(7 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board180(self):
        ans0 = Label(f5, text='(8 , 0)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board181(self):
        ans0 = Label(f5, text='(8 , 1)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board182(self):
        ans0 = Label(f5, text='(8 , 2)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board183(self):
        ans0 = Label(f5, text='(8 , 3)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board184(self):
        ans0 = Label(f5, text='(8 , 4)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board185(self):
        ans0 = Label(f5, text='(8 , 5)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board186(self):
        ans0 = Label(f5, text='(8 , 6)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board187(self):
        ans0 = Label(f5, text='(8 , 7)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)

    def board188(self):
        ans0 = Label(f5, text='(8 , 8)', font=("Arial", 30), fg="gray")
        ans0.place(x=830, y=180)
    #-------

#--------------------------------------------------------------


# ------------------------------------- frame0 -------------------------------------
def des_f0():
    f0.destroy()

# function defined to show rules
def show_rules():
    mbox.showinfo("RULES", "1.)  There will be 5 Levels.\n\n2.)  For each level Player need to first click on that level button and  find the position of odd symbol(one which is different from all other) in the given level board.\n\n3.)  The points each level will be shown at the top right corner.\n\n4.)  At last, final score will be shown along with count of correct and wrong answer.")

# created first main frame
f0 = Frame(root, height=780, width=1000)
f0.propagate(0)
f0.pack(side='top')

# function for adding image in frame 1
c = Canvas(f0, width=1000, height=700)
c.pack()
p1 = PhotoImage(file='Images/odd_symbol.gif')
c.create_image(70, 130, image=p1, anchor=NW)

# for starting top label
top0 = Label(f0, text='ODD SYMBOL FIND', font=("Arial", 60), fg="magenta", underline = 0)
top0.place(x=120, y=10)

# created start button
startb = Button(f0, text="START",command=des_f0,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
startb.place(x = 150 , y =600 )

# created start button
rulesb = Button(f0, text="RULES",command=show_rules,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
rulesb.place(x = 450 , y =600 )

# ------------------------- frame1 - level1 --------------------------------------
def des_f1():
    f1.destroy()

# created frame 1
f1 = Frame(root, height=780, width=1000)
f1.propagate(0)
f1.pack(side='top')
level1 = Level1_keypad(root)

# text area created
text_enter = tk.Text(f1, height=2, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.insert(END, 'Write Your Code Here...') # default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
# text_enter.place(x=50, y=10)

# keyboard button created for opening keyboard
level1b = Button(f1, text="LEVEL-1",command=lambda:level1.show(text_enter),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
level1b.place(x =100 , y =600 )

# label for showing points on tp right corner
points1 = Label(f1, text="Points : " + str(10), font=("Arial", 35), fg="magenta")
points1.place(x = 700, y = 20)

# for starting top label
selected1 = Label(f1, text='CELL : ', font=("Arial", 30), fg="brown")
selected1.place(x=700, y=180)

# for telling top label
tell1 = Label(f1, text='Click on cell\nwith odd\nsymbol', font=("Arial", 30), fg="blue")
tell1.place(x=700, y=300)

# keyboard button created for opening keyboard
nextb = Button(f1, text="NEXT",command=des_f1,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nextb.place(x =450 , y =600 )
# -------------------------------------------------------------------------------------

# ------------------------- frame2 - level2 --------------------------------------
def des_f2():
    f2.destroy()

f2 = Frame(root, height=780, width=1000)
f2.propagate(0)
f2.pack(side='top')
level2 = Level2_keypad(root)

# text area created
text_enter = tk.Text(f2, height=2, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.insert(END, 'Write Your Code Here...') # default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
# text_enter.place(x=50, y=10)

# keyboard button created for opening keyboard
level2b = Button(f2, text="LEVEL-2",command=lambda:level2.show(text_enter),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
level2b.place(x =100 , y =600 )

points2 = Label(f2, text="Points : " + str(15), font=("Arial", 35), fg="magenta")
points2.place(x = 700, y = 20)

# for starting top label
selected2 = Label(f2, text='CELL : ', font=("Arial", 30), fg="brown")
selected2.place(x=700, y=180)

# for telling top label
tell1 = Label(f2, text='Click on cell\nwith odd\nsymbol', font=("Arial", 30), fg="blue")
tell1.place(x=700, y=300)

# keyboard button created for opening keyboard
nextb = Button(f2, text="NEXT",command=des_f2,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nextb.place(x =450 , y =600 )
# -------------------------------------------------------------------------------------

# ------------------------- frame3 - level3 --------------------------------------
def des_f3():
    f3.destroy()

f3 = Frame(root, height=780, width=1000)
f3.propagate(0)
f3.pack(side='top')
level3 = Level3_keypad(root)

# text area created
text_enter = tk.Text(f3, height=2, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.insert(END, 'Write Your Code Here...') # default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
# text_enter.place(x=50, y=10)

# keyboard button created for opening keyboard
level3b = Button(f3, text="LEVEL-3",command=lambda:level3.show(text_enter),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
level3b.place(x =100 , y =600 )

points3 = Label(f3, text="Points : " + str(20), font=("Arial", 35), fg="magenta")
points3.place(x = 700, y = 20)

# for starting top label
selected3 = Label(f3, text='CELL : ', font=("Arial", 30), fg="brown")
selected3.place(x=700, y=180)

# for telling top label
tell1 = Label(f3, text='Click on cell\nwith odd\nsymbol', font=("Arial", 30), fg="blue")
tell1.place(x=700, y=300)

# keyboard button created for opening keyboard
nextb = Button(f3, text="NEXT",command=des_f3,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nextb.place(x =450 , y =600 )
# -------------------------------------------------------------------------------------

# ------------------------- frame4 - level4 --------------------------------------
def des_f4():
    f4.destroy()

f4 = Frame(root, height=780, width=1000)
f4.propagate(0)
f4.pack(side='top')
level4 = Level4_keypad(root)

# text area created
text_enter = tk.Text(f4, height=2, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.insert(END, 'Write Your Code Here...') # default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
# text_enter.place(x=50, y=10)

# keyboard button created for opening keyboard
level4b = Button(f4, text="LEVEL-4",command=lambda:level4.show(text_enter),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
level4b.place(x =100 , y =600 )

points1 = Label(f4, text="Points : " + str(25), font=("Arial", 35), fg="magenta")
points1.place(x = 700, y = 20)

# for starting top label
selected4 = Label(f4, text='CELL : ', font=("Arial", 30), fg="brown")
selected4.place(x=700, y=180)

# for telling top label
tell1 = Label(f4, text='Click on cell\nwith odd\nsymbol', font=("Arial", 30), fg="blue")
tell1.place(x=700, y=300)

# keyboard button created for opening keyboard
nextb = Button(f4, text="NEXT",command=des_f4,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nextb.place(x =450 , y =600 )
# -------------------------------------------------------------------------------------

# ------------------------- frame5 - level5 --------------------------------------
def des_f5():
    f5.destroy()
    # -------------------------------------------------------------------------------------

    f6 = Frame(root, height=780, width=1000)
    f6.propagate(0)
    f6.pack(side='top')

    cnt = 0
    cr = 0
    wr = 0
    # print(ans1,ans2,ans3,ans4,ans5)
    if(ans1 == 1):
        cnt = cnt + 10
        cr = cr + 1
    else:
        wr = wr + 1
    if(ans2 == 1):
        cnt = cnt + 15
        cr = cr + 1
    else:
        wr = wr + 1
    if(ans3 == 1):
        cnt = cnt + 20
        cr = cr + 1
    else:
        wr = wr + 1
    if(ans4 == 1):
        cnt = cnt + 25
        cr = cr + 1
    else:
        wr = wr + 1
    if(ans5 == 1):
        cnt = cnt + 30
        cr = cr + 1
    else:
        wr = wr + 1

    c3 = Canvas(f6, width=1000, height=700, bg="white")  # blue
    c3.pack()
    p3 = PhotoImage(file="Images/score1.gif")
    c3.create_image(300, 10, image=p3, anchor="nw")
    w3 = Canvas(root)
    w3.p3 = p3

    score1 = Label(f6, text=str(cnt) + "/100", font=("Arial", 100), fg="green", bg="white")
    score1.place(x=250, y=230)

    correct1 = Label(f6, text ="Correct Answer : " + str(cr) + "/5", font=("Arial", 40), fg="brown", bg="white")
    correct1.place(x=230, y=430)

    wrong1 = Label(f6, text="Wrong Answer : " + str(wr) + "/5", font=("Arial", 40), fg="brown", bg="white")
    wrong1.place(x=230, y=530)

    # ----------------------------------------------------------------------------

f5 = Frame(root, height=780, width=1000)
f5.propagate(0)
f5.pack(side='top')
level5 = Level5_keypad(root)

# text area created
text_enter = tk.Text(f5, height=2, width=80, font=("Arial", 15), bg="light yellow", fg="brown",borderwidth=3, relief="solid")
text_enter.insert(END, 'Write Your Code Here...') # default line in text area, can be cleared when touched
# text_enter.bind('<FocusIn>', on_text_enter_click)
# text_enter.place(x=50, y=10)

# keyboard button created for opening keyboard
level5b = Button(f5, text="LEVEL-5",command=lambda:level5.show(text_enter),font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
level5b.place(x =100 , y =600 )

points5 = Label(f5, text="Points : " + str(30), font=("Arial", 35), fg="magenta")
points5.place(x = 700, y = 20)

# for starting top label
selected5 = Label(f5, text='CELL : ', font=("Arial", 30), fg="brown")
selected5.place(x=700, y=180)

# for telling top label
tell1 = Label(f5, text='Click on cell\nwith odd\nsymbol', font=("Arial", 30), fg="blue")
tell1.place(x=700, y=300)

# keyboard button created for opening keyboard
nextb = Button(f5, text="SCORE",command=des_f5,font=("Arial", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
nextb.place(x =450 , y =600 )


# function for exiting
def exit_win():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# created exit button
exitb = Button(root, text="EXIT",command=exit_win,font=("Arial", 20), bg = "red", fg = "blue", borderwidth=3, relief="raised")
exitb.place(x =750 , y =600 )


root.protocol("WM_DELETE_WINDOW", exit_win)
root.mainloop()
