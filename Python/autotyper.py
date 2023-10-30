import re
from pynput.keyboard import Controller
from tkinter import *
import tkinter as tk
import time
import keyboard as kb
import webbrowser
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("res")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = Tk()
#Windows Title
root.title("AutoTyper")
root.geometry("600x400")
root.resizable(0,0)
root.configure(bg = "#BCEAD5")

#windows icon set
photo = PhotoImage(file="res/icons.png")

root.iconphoto(False, photo)


keyboard = Controller()

fontSmall= ('', 8)
cursor="hand2"

def callback(event):
    webbrowser.open_new_tab(event)

def rTime():
    time.sleep(4)
def rTime1():
    time.sleep(1)

def paste():
    input1=entry.get(1.0, tk.END+"-1c")
    rTime()
    keyboard.type(input1)

def paste1():
    input1=entry.get(1.0, tk.END+"-1c")
    rTime1()
    keyboard.type(input1)

def linebyline():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def singleline():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def linebyline1():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)

def singleline2():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)


canvas = Canvas(
    root,
    bg = "#D2DAFF",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    300.5,
    154.0,
    image=entry_image_1
)
entry = Text(
    bd=0,
    bg="#EEF1FF",
    highlightthickness=0
)
entry.place(
    x=19.0,
    y=6.0,
    width=570.0,
    height=294.0
)

kb.add_hotkey('ctrl+6', paste1)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=singleline,
    relief="flat"
)
button_2.place(
    x=200.0,
    y=320.0,
    width=148.0,
    height=47.0
)

kb.add_hotkey('ctrl+7', singleline2)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=linebyline,
    relief="flat"
)
button_3.place(
    x=400.0,
    y=320.0,
    width=148.0,
    height=47.0
)

kb.add_hotkey('ctrl+8', linebyline1)

canvas.create_text(
    6.0,
    380.0,
    anchor="nw",
    text="Crafted With 🖤",
    fill="#666699",
    font=("Corbel", 7 * -2)
)
canvas.create_text(
    515.0,
    380.0,
    anchor="nw",
    text="@Sajansharma0017",
    fill="#666699",
    font=("Corbel", 7 * -2)
)

lbl = Label(root, text="ㅤGithubㅤ",fg='white',bg="#546E7A", highlightthickness=5,highlightbackground = "#546E7A", font=('Corbel',18, 'bold'))
lbl.place(x=20, y=320)
lbl.bind("<Button>", lambda e: callback("https://github.com/Sajansharma0017"))

root.attributes('-topmost', True)

root.mainloop()