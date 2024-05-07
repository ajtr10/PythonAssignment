from tkinter import *
from math import *

class NormalCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg="#023872")

        self.my_entry = Entry(root, width=30, borderwidth=3)
        self.my_entry.grid(row=0, column=0, columnspan=4, pady=5, padx=10)

        self.create_buttons()

    def text_change(self, token):
        if token != "=":
            self.my_entry.insert(END, token)
        else:
            result = str(eval(self.my_entry.get()))
            self.my_entry.delete(0, END)
            self.my_entry.insert(0, result)

    def clear_text(self):
        self.my_entry.delete(0, END)

    def create_buttons(self):
        button0 = Button(self.root, text="0", command=lambda: self.text_change("0"), height=5, width=10, background="#a2e1e8")
        button1 = Button(self.root, text="1", command=lambda: self.text_change("1"), height=5, width=10, background="#a2e1e8")
        button2 = Button(self.root, text="2", command=lambda: self.text_change("2"), height=5, width=10, background="#a2e1e8")
        button3 = Button(self.root, text="3", command=lambda: self.text_change("3"), height=5, width=10, background="#a2e1e8")
        button4 = Button(self.root, text="4", command=lambda: self.text_change("4"), height=5, width=10, background="#a2e1e8")
        button5 = Button(self.root, text="5", command=lambda: self.text_change("5"), height=5, width=10, background="#a2e1e8")
        button6 = Button(self.root, text="6", command=lambda: self.text_change("6"), height=5, width=10, background="#a2e1e8")
        button7 = Button(self.root, text="7", command=lambda: self.text_change("7"), height=5, width=10, background="#a2e1e8")
        button8 = Button(self.root, text="8", command=lambda: self.text_change("8"), height=5, width=10, background="#a2e1e8")
        button9 = Button(self.root, text="9", command=lambda: self.text_change("9"), height=5, width=10, background="#a2e1e8")
        button_plus = Button(self.root, text="+", command=lambda: self.text_change("+"), height=5, width=10, background="#2277a6")
        button_minus = Button(self.root, text="-", command=lambda: self.text_change("-"), height=5, width=10, background="#2277a6")
        button_multiply = Button(self.root, text="*", command=lambda: self.text_change("*"), height=5, width=10, background="#2277a6")
        button_divide = Button(self.root, text="/", command=lambda: self.text_change("/"), height=5, width=10, background="#2277a6")
        button_equal = Button(self.root, text="=", command=lambda: self.text_change("="), height=5, width=10, background="#2277a6")
        button_decimal = Button(self.root, text=".", command=lambda: self.text_change("."), height=5, width=10, background="#a2e1e8")
        button_sin = Button(self.root, text="sin", command=lambda: self.text_change("sin("), height=5, width=10, background="#2277a6")
        button_cos = Button(self.root, text="cos", command=lambda: self.text_change("cos("), height=5, width=10, background="#2277a6")
        button_tan = Button(self.root, text="tan", command=lambda: self.text_change("tan("), height=5, width=10, background="#2277a6")
        button_cot = Button(self.root, text="cot", command=lambda: self.text_change("cot("), height=5, width=10, background="#2277a6")
        button_clear = Button(self.root, text="Clear", command=self.clear_text, height=5, width=10, background="#2277a6")
        button_leftbracket = Button(self.root, text="(", command=lambda: self.text_change("("), height=5, width=10, background="#a2e1e8")
        button_rightbracket = Button(self.root, text=")", command=lambda: self.text_change(")"), height=5, width=10, background="#a2e1e8")
        button_log = Button(self.root, text="log", command=lambda: self.text_change("log("), height=5, width=10, background="#2277a6")
        button_expo = Button(self.root, text="exponent", command=lambda: self.text_change("**"), height=5, width=10, background="#2277a6")

        button0.grid(row=1, column=0)
        button1.grid(row=1, column=1)
        button2.grid(row=1, column=2)
        button3.grid(row=2, column=0)
        button4.grid(row=2, column=1)
        button5.grid(row=2, column=2)
        button6.grid(row=3, column=0)
        button7.grid(row=3, column=1)
        button8.grid(row=3, column=2)
        button9.grid(row=4, column=0)
        button_plus.grid(row=1, column=3)
        button_minus.grid(row=1, column=5)
        button_multiply.grid(row=2, column=3)
        button_divide.grid(row=2, column=5)
        button_equal.grid(row=3, column=3)
        button_decimal.grid(row=4, column=1)
        button_sin.grid(row=5, column=0)
        button_cos.grid(row=5, column=1)
        button_tan.grid(row=5, column=2)
        button_cot.grid(row=5, column=3)
        button_clear.grid(row=3, column=5)
        button_leftbracket.grid(row=4, column=1)
        button_rightbracket.grid(row=4, column=2)
        button_log.grid(row=4, column=3)
        button_expo.grid(row=4, column=5)

if __name__ == "__main__":
    main_window = Tk()
    app = NormalCalculator(main_window)
    main_window.mainloop()
