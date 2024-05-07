import tkinter as tk
from tkinter import ttk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        self.equation = ""

        # Entry field to display and input expressions
        self.entry = ttk.Entry(root, font=('Arial', 20), width=25, justify='right')
        self.entry.grid(row=0, column=0, columnspan=6)

        # Buttons for numbers and operators
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('(', 1, 4), (')', 1, 5), ('%', 2, 4), ('^', 2, 5),
            ('√', 3, 4), ('sin', 3, 5), ('cos', 4, 4), ('tan', 4, 5),
            ('asin', 5, 0), ('acos', 5, 1), ('atan', 5, 2), ('log', 5, 3),
            ('ln', 5, 4), ('π', 5, 5), ('C', 6, 0)
        ]

        for (text, row, col) in buttons:
            ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

    def on_button_click(self, value):
        if value == '=':
            self.calculate_result()
        elif value == 'C':
            self.equation = ""
            self.update_display()
        elif value == '√':
            self.equation += 'math.sqrt('
            self.update_display()
        elif value in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan'):
            self.equation += f'math.{value}('
            self.update_display()
        elif value == 'π':
            self.equation += 'math.pi'
            self.update_display()
        elif value == '^':
            self.equation += '**'
            self.update_display()
        elif value == 'log':
            self.equation += 'math.log('
            self.update_display()
        elif value == 'ln':
            self.equation += 'math.log('
            self.update_display()
        elif value == '%':
            self.equation += '/100'
            self.update_display()
        else:
            self.equation += value
            self.update_display()

    def calculate_result(self):
        try:
            result = eval(self.equation)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            print(e)

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.equation)

# Create the main window
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
