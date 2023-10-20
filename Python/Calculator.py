import tkinter as tk

def button_click(item):
    global expression
    expression = expression + str(item)
    equation.set(expression)

def button_clear():
    global expression
    expression = ""
    equation.set("")

def button_equal():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""

# Create the main application window
root = tk.Tk()
root.geometry("240x150")
root.title("Simple Calculator")

expression = ""
equation = tk.StringVar()

# Create the entry widget for the calculator display
entry = tk.Entry(root, textvariable=equation, width=20, font=("Arial", 15))
entry.grid(row=0, columnspan=4)

# Create and configure buttons for the calculator
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_index = 1
col_index = 0
for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, command=lambda: button_clear(), width=5).grid(row=row_index, column=col_index)
    elif button == '=':
        tk.Button(root, text=button, command=lambda: button_equal(), width=5).grid(row=row_index, column=col_index)
    else:
        tk.Button(root, text=button, command=lambda x=button: button_click(x), width=5).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

# Run the main event loop
root.mainloop()
