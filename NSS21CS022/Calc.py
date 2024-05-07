import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.display = tk.Entry(master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("sqrt", 5, 3),
            ("log", 6, 0), ("log10", 6, 1), ("pi", 6, 2), ("e", 6, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, width=5, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "sqrt":
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == "pi":
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
        elif value == "log10":
            try:
                result = math.log10(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
