import tkinter as tk
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("580x530")
root.configure(bg="#000000")

calc_operator = ""
text_input = tk.StringVar()

entry = tk.Entry(root, textvariable=text_input, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right', bg="#333333", fg="white")
entry.grid(row=0, column=0, columnspan=10, pady=20)

def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1 / math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def button_log10():
    global calc_operator
    result = str(math.log10(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_ln():
    global calc_operator
    result = str(math.log(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_deg():
    global calc_operator
    result = str(math.degrees(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_rad():
    global calc_operator
    result = str(math.radians(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_cosh():
    global calc_operator
    result = str(math.cosh(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_tanh():
    global calc_operator
    result = str(math.tanh(float(calc_operator)))
    calc_operator = result
    text_input.set(result)

def button_sinh():
    global calc_operator
    result = str(math.sinh(float(calc_operator)))
    calc_operator = result
    text_input.set(result)


def square_root():
    global calc_operator
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def cube_root():
    global calc_operator
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def sign_change():
    global calc_operator
    if calc_operator[0] == '-':
        temp = calc_operator[1:]
    else:
        temp = '-' + calc_operator
    calc_operator = temp
    text_input.set(temp)

def percent():
    global calc_operator
    temp = str(eval(calc_operator + '/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op

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

button_width = 3
button_height = 2

for btn_text, command in buttons:
    if btn_text.isdigit() or btn_text == ".":
        bg_color = "#53777A"
        fg_color = "#FFFFFF"
    elif btn_text in ["AC", "DEL"]:
        bg_color = "orange"
        fg_color = "black"
    else:
        bg_color = "#88C088"
        fg_color = "black"
        
    tk.Button(root, text=btn_text, font=('Arial', 16), padx=10, pady=10, command=command, bg=bg_color, fg=fg_color, bd=0, width=button_width, height=button_height).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 7:
        col = 0
        row += 1

root.mainloop()
