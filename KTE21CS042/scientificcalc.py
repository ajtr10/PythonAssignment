import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.entry = tk.Entry(master, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=6)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4), ('AC', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4), (')', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('π', 3, 4), ('^', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('√', 4, 4), ('%', 4, 5),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('asin', 5, 3), ('acos', 5, 4), ('atan', 5, 5)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=20, pady=10, command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, value):
        if value == 'C':
            self.entry.delete(len(self.entry.get()) - 1)
        elif value == 'AC':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif value == 'π':
            self.entry.insert(tk.END, math.pi)
        elif value == '√':
            self.entry.insert(tk.END, 'sqrt(')
        elif value == '^':
            self.entry.insert(tk.END, '**')
        elif value == '%':
            self.entry.insert(tk.END, '/100')
        elif value == 'sin':
            self.entry.insert(tk.END, 'math.sin(math.radians(')
        elif value == 'cos':
            self.entry.insert(tk.END, 'math.cos(math.radians(')
        elif value == 'tan':
            self.entry.insert(tk.END, 'math.tan(math.radians(')
        elif value == 'asin':
            self.entry.insert(tk.END, 'math.degrees(math.asin(')
        elif value == 'acos':
            self.entry.insert(tk.END, 'math.degrees(math.acos(')
        elif value == 'atan':
            self.entry.insert(tk.END, 'math.degrees(math.atan(')
        else:
            self.entry.insert(tk.END, value)

def main():
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
