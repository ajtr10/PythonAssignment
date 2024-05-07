import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("680x630")  # Adjusted window size
root.configure(bg="#F0F0F0")  # Changing background color

operation = ""
text_input = tk.StringVar()

entry = tk.Entry(root, textvariable=text_input, font=('Arial', 20), bd=10, insertwidth=4, width=20, justify='right', bg="#FFFFFF", fg="black")  # Adjusted entry width
entry.grid(row=0, column=0, columnspan=10, pady=20)

def button_click(char):
    global operation
    operation += str(char)
    text_input.set(operation)

def button_clear_all():
    global operation
    operation = ""
    text_input.set("")

def button_delete():
    global operation
    text = operation[:-1]
    operation = text
    text_input.set(text)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def fact_func():
    global operation
    result = str(factorial(int(operation)))
    operation = result
    text_input.set(result)

def trig_sin():
    global operation
    result = str(math.sin(math.radians(int(operation))))
    operation = result
    text_input.set(result)

def trig_cos():
    global operation
    result = str(math.cos(math.radians(int(operation))))
    operation = result
    text_input.set(result)

def trig_tan():
    global operation
    result = str(math.tan(math.radians(int(operation))))
    operation = result
    text_input.set(result)

def trig_cot():
    global operation
    result = str(1 / math.tan(math.radians(int(operation))))
    operation = result
    text_input.set(result)

def button_log10():
    global operation
    result = str(math.log10(float(operation)))
    operation = result
    text_input.set(result)

def button_ln():
    global operation
    result = str(math.log(float(operation)))
    operation = result
    text_input.set(result)

def button_deg():
    global operation
    result = str(math.degrees(float(operation)))
    operation = result
    text_input.set(result)

def button_rad():
    global operation
    result = str(math.radians(float(operation)))
    operation = result
    text_input.set(result)

def button_cosh():
    global operation
    result = str(math.cosh(float(operation)))
    operation = result
    text_input.set(result)

def button_tanh():
    global operation
    result = str(math.tanh(float(operation)))
    operation = result
    text_input.set(result)

def button_sinh():
    global operation
    result = str(math.sinh(float(operation)))
    operation = result
    text_input.set(result)


def square_root():
    global operation
    if int(operation) >= 0:
        temp = str(eval(operation + '**(1/2)'))
        operation = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def cube_root():
    global operation
    if int(operation) >= 0:
        temp = str(eval(operation + '**(1/3)'))
        operation = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def sign_change():
    global operation
    if operation[0] == '-':
        temp = operation[1:]
    else:
        temp = '-' + operation
    operation = temp
    text_input.set(temp)

def percent():
    global operation
    temp = str(eval(operation + '/100'))
    operation = temp
    text_input.set(temp)

def button_equal():
    global operation
    temp_op = str(eval(operation))
    text_input.set(temp_op)
    operation = temp_op

buttons = [
    ("AC", button_clear_all),
    ("DEL", button_delete),
    ("√", square_root),
    ("+", lambda: button_click("+")),
    ("π", lambda: button_click(math.pi)),
    ("cosθ", trig_cos),
    ("tanθ", trig_tan),
    ("sinθ", trig_sin),
    ("1", lambda: button_click(1)),
    ("2", lambda: button_click(2)),
    ("3", lambda: button_click(3)),
    ("-", lambda: button_click("-")),
    ("2π", lambda: button_click(2 * math.pi)),
    ("cosh", button_cosh),
    ("tanh", button_tanh),
    ("sinh", button_sinh),
    ("4", lambda: button_click(4)),
    ("5", lambda: button_click(5)),
    ("6", lambda: button_click(6)),
    ("*", lambda: button_click("*")),
    (chr(8731), cube_root),
    ("x\u02b8", lambda: button_click("**")),
    ("x\u00B3", lambda: button_click("**3")),
    ("x\u00B2", lambda: button_click("**2")),
    ("7", lambda: button_click(7)),
    ("8", lambda: button_click(8)),
    ("9", lambda: button_click(9)),
    (chr(247), lambda: button_click("/")),
    ("ln", button_ln),
    ("deg", button_deg),
    ("rad", button_rad),
    ("e", lambda: button_click(math.e)),
    ("0", lambda: button_click(0)),
    (".", lambda: button_click(".")),
    ("%", percent),
    ("=", button_equal),
    ("log10", button_log10),
    ("(", lambda: button_click("(")),
    (")", lambda: button_click(")")),
    ("x!", fact_func),
]

row = 1
col = 0

button_width = 4  # Adjusted button width
button_height = 3  # Adjusted button height

for btn_text, command in buttons:
    if btn_text.isdigit() or btn_text == ".":
        bg_color = "#4CAF50"  # Changed button color
        fg_color = "#FFFFFF"
    else:
        bg_color = "#607D8B"  # Changed button color
        fg_color = "#FFFFFF"
        
    tk.Button(root, text=btn_text, font=('Arial', 16), padx=10, pady=10, command=command, bg=bg_color, fg=fg_color, bd=0, width=button_width, height=button_height).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 7:
        col = 0
        row += 1

root.mainloop()
