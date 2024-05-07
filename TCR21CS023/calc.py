import tkinter as tk
import math

def evaluate(event):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear(event):
    entry.delete(0, tk.END)

def insert_text(event):
    entry.insert(tk.END, event.widget.cget("text"))

def square_root(event):
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sin(event):
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cos(event):
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tan(event):
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def arcsin(event):
    try:
        result = math.degrees(math.asin(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def arccos(event):
    try:
        result = math.degrees(math.acos(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def arctan(event):
    try:
        result = math.degrees(math.atan(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def log(event):
    try:
        result = math.log(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def exp(event):
    try:
        result = math.exp(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def power(event):
    try:
        result = eval(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, font=("Helvetica", 16))
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "sqrt",
    "1", "2", "3", "-", "(",
    "0", ".", "=", "+", ")",
    "sin", "cos", "tan", "arcsin", "arccos",
    "arctan", "log", "exp", "^"
]

row = 1
col = 0
for button_text in buttons:
    if col == 5:
        col = 0
        row += 1
    button = tk.Button(root, text=button_text, font=("Helvetica", 12))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", insert_text)
    if button_text == "C":
        button.bind("<Button-1>", clear)
    elif button_text == "=":
        button.bind("<Button-1>", evaluate)
    elif button_text == "sqrt":
        button.bind("<Button-1>", square_root)
    elif button_text == "sin":
        button.bind("<Button-1>", sin)
    elif button_text == "cos":
        button.bind("<Button-1>", cos)
    elif button_text == "tan":
        button.bind("<Button-1>", tan)
    elif button_text == "arcsin":
        button.bind("<Button-1>", arcsin)
    elif button_text == "arccos":
        button.bind("<Button-1>", arccos)
    elif button_text == "arctan":
        button.bind("<Button-1>", arctan)
    elif button_text == "log":
        button.bind("<Button-1>", log)
    elif button_text == "exp":
        button.bind("<Button-1>", exp)
    elif button_text == "^":
        button.bind("<Button-1>", power)
    col += 1

root.mainloop()