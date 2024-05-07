import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.display = tk.Entry(root, width=20, font=("Helvetica", 30))
        self.display.grid(row=0, column=0, columnspan=4, pady=5, padx=1)

        self.render_buttons()
        tk.Label(root, text="Aqeel, RollNo.69, LTCR21CS071", font=("Helvetica", 14)).grid(row=7, column=0, columnspan=4)

    def render_buttons(self):
        buttons = [
            ("7", 1, 0, "lightgrey"), ("8", 1, 1, "lightgrey"), ("9", 1, 2, "lightgrey"), ("÷", 1, 3, "orange"),
            ("4", 2, 0, "lightgrey"), ("5", 2, 1, "lightgrey"), ("6", 2, 2, "lightgrey"), ("x", 2, 3, "orange"),
            ("1", 3, 0, "lightgrey"), ("2", 3, 1, "lightgrey"), ("3", 3, 2, "lightgrey"), ("-", 3, 3, "orange"),
            ("0", 4, 0, "lightgrey"), (".", 4, 1, "lightgrey"), ("√", 4, 2, "grey"), ("+", 4, 3, "orange"),
            ("sin", 5, 0, "grey"), ("cos", 5, 1, "grey"), ("tan", 5, 2, "grey"), ("=", 5, 3, "orange"),
            ("log", 6, 0, "grey"), ("π", 6, 1, "grey"), ("e", 6, 2, "grey"), ("C", 6, 3, "orange"),
        ]

        for (text, row, col, color) in buttons:
            button = tk.Button(self.root, text=text, width=5, height=2, font=("Helvetica", 20), command=lambda x=text: self.btn_onclick(x), highlightbackground=color)
            button.grid(row=row, column=col, padx=0, pady=2)

    def btn_onclick(self, value):
        if value == "=":
            try:
                result = eval(self.display.get().replace("÷", "/").replace("x", "*"))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "√":
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "π":
            self.display.insert(tk.END, math.pi)
        elif value == "e":
            self.display.insert(tk.END, math.e)
        elif value == "sin":
            try:
                result = math.sin(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "cos":
            try:
                result = math.cos(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "tan":
            try:
                result = math.tan(math.radians(float(self.display.get())))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "log":
            try:
                result = math.log(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "C":
                self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, value)


root = tk.Tk()
calculator = Calculator(root)
root.title("Scientific Calculator")
root.mainloop()