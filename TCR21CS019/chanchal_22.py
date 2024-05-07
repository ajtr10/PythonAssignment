import tkinter
import math

def click(val):
    e = entry.get() 
    ans = " "

    try:
        if val == "C":
            e = e[0:len(e) - 1]  
            entry.delete(0, "end")
            entry.insert(0, e)
            return

        elif val == "CE":
            entry.delete(0, "end")

        elif val == "√":
            ans = math.sqrt(eval(e))

        elif val == "π":
            ans = math.pi

        elif val == "cosθ":
            ans = math.cos(math.radians(eval(e)))

        elif val == "sinθ":
            ans = math.sin(math.radians(eval(e)))

        elif val == "tanθ":
            ans = math.tan(math.radians(eval(e)))

        elif val == "2π":
            ans = 2 * math.pi

        elif val == "cosh":
            ans = math.cosh(eval(e))

        elif val == "sinh":
            ans = math.sinh(eval(e))

        elif val == "tanh":
            ans = math.tanh(eval(e))

        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)

        elif val == "x\u02b8":
            entry.insert("end", "**")
            return

        elif val == "x\u00B3":
            ans = eval(e) ** 3

        elif val == "x\u00B2":
            ans = eval(e) ** 2

        elif val == "ln":
            ans = math.log2(eval(e))

        elif val == "deg":
            ans = math.degrees(eval(e))

        elif val == "rad":
            ans = math.radians(eval(e))

        elif val == "e":
            ans = math.e

        elif val == "log10":
            ans = math.log10(eval(e))

        elif val == "x!":
            ans = math.factorial(eval(e))

        elif val == chr(247):
            entry.insert("end", "/")
            return

        elif val == "=":
            ans = eval(e)

        else:
            entry.insert("end", val)
            return

        entry.delete(0, "end")
        entry.insert(0, ans)

    except SyntaxError:
        print("Error")
       

root = tkinter.Tk()
root.title("Scientific Calculator")
root.geometry("680x486+100+100")
root.config(bg="grey")

entry = tkinter.Entry(root, font=("arial", 20, "bold"), bg="white", fg="black", bd=10, width=40)
entry.grid(row=0, column=0, columnspan=8, pady=5)

buttons = {
    "C": (1, 0), "CE": (1, 1), "√": (1, 2), "+": (1, 3), "π": (1, 4),
    "cosθ": (1, 5), "tanθ": (1, 6), "sinθ": (1, 7), "1": (2, 0), "2": (2, 1),
    "3": (2, 2), "-": (2, 3), "2π": (2, 4), "cosh": (2, 5), "tanh": (2, 6),
    "sinh": (2, 7), "4": (3, 0), "5": (3, 1), "6": (3, 2), "*": (3, 3),
    chr(8731): (3, 4), "x\u02b8": (3, 5), "x\u00B3": (3, 6), "x\u00B2": (3, 7),
    "7": (4, 0), "8": (4, 1), "9": (4, 2), chr(247): (4, 3), "ln": (4, 4),
    "deg": (4, 5), "rad": (4, 6), "e": (4, 7), "0": (5, 0), ".": (5, 1),
    "%": (5, 2), "=": (5, 3), "log10": (5, 4), "(": (5, 5), ")": (5, 6),
    "x!": (5, 7)
}

for key, (row, col) in buttons.items():
    button = tkinter.Button(root, width=5, height=2, bd=2, text=key, bg="white", fg="black",
                            font=("arial", 18, "bold"), command=lambda button=key: click(button))
    button.grid(row=row, column=col, pady=2)

root.mainloop()
