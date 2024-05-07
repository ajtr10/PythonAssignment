import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.configure(background='white')  # Set background color
        self.create_widgets()

    def create_widgets(self):
        # Create a text entry widget to display and input values
        self.result_var = tk.StringVar()
        self.result_var.set("")
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 14), bd=5, relief=tk.SUNKEN, justify=tk.RIGHT)
        result_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')

        # Create buttons for calculator functions and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('^', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3), ('π', 5, 4)
        ]

        # Create buttons and place them on the grid
        for (text, row, col) in buttons:
            btn = tk.Button(self, text=text, font=('Arial', 14), padx=10, pady=10, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Make grid cells expandable to fit the screen
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        # Handle button clicks and update the display accordingly
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif char == 'C':
            self.result_var.set("")
        elif char == 'π':
            self.result_var.set(math.pi)
        elif char == '√':
            self.result_var.set(math.sqrt(float(self.result_var.get())))
        elif char == 'sin':
            self.result_var.set(math.sin(math.radians(float(self.result_var.get()))))
        elif char == 'cos':
            self.result_var.set(math.cos(math.radians(float(self.result_var.get()))))
        elif char == 'tan':
            self.result_var.set(math.tan(math.radians(float(self.result_var.get()))))
        elif char == '^':
            self.result_var.set(self.result_var.get() + '**')
        else:
            self.result_var.set(self.result_var.get() + char)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
