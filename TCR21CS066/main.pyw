from tkinter import *
from matrix_calculator import MatrixCalculator
from normal_calculator import NormalCalculator

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator App")
        self.root.configure(bg="#023872")

        # Create buttons for switching between calculators
        self.normal_calc_button = Button(root, text="Normal Calculator", command=self.switch_to_normal, bg="#2277a6", fg="white")
        self.normal_calc_button.pack(pady=10)

        self.matrix_calc_button = Button(root, text="Matrix Calculator", command=self.switch_to_matrix, bg="#2277a6", fg="white")
        self.matrix_calc_button.pack(pady=10)

    def switch_to_normal(self):
        self.root.destroy()
        root = Tk()
        app = NormalCalculator(root)
        root.mainloop()

    def switch_to_matrix(self):
        self.root.destroy()
        root = Tk()
        app = MatrixCalculator(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = CalculatorApp(root)
    root.mainloop()
