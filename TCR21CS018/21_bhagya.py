import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=('Arial', 18))
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('cot', 5, 3),
            ('√', 6, 0), ('x²', 6, 1), ('x³', 6, 2), ('DEL', 6, 3),
            ('C', 7, 0), ('π', 7, 1), ('e', 7, 2), ('(', 7, 3),
            (')', 8, 0), ('^', 8, 1), ('log', 8, 2), ('ln', 8, 3),
            ('asin', 9, 0), ('acos', 9, 1), ('atan', 9, 2), ('%', 9, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self, text=text, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char == 'DEL':
            text = self.display.get()[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, text)
        elif char == 'sin':
            self.display.insert(tk.END, 'math.sin(')
        elif char == 'cos':
            self.display.insert(tk.END, 'math.cos(')
        elif char == 'tan':
            self.display.insert(tk.END, 'math.tan(')
        elif char == 'cot':
            self.display.insert(tk.END, '1/math.tan(')
        elif char == '√':
            self.display.insert(tk.END, '**0.5')
        elif char == 'x²':
            self.display.insert(tk.END, '**2')
        elif char == 'x³':
            self.display.insert(tk.END, '**3')
        elif char == 'π':
            self.display.insert(tk.END, 'math.pi')
        elif char == 'e':
            self.display.insert(tk.END, 'math.e')
        elif char == 'log':
            self.display.insert(tk.END, 'math.log(')
        elif char == 'ln':
            self.display.insert(tk.END, 'math.log(')
        elif char == 'asin':
            self.display.insert(tk.END, 'math.asin(')
        elif char == 'acos':
            self.display.insert(tk.END, 'math.acos(')
        elif char == 'atan':
            self.display.insert(tk.END, 'math.atan(')
        elif char == '%':
            self.display.insert(tk.END, '/100')
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
