import tkinter as tk
import math



root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")
root.configure(bg="#333333")

calc_operator = ""

text_input = tk.StringVar()


entry = tk.Entry(root, textvariable=text_input, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right', bg="#333333", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=20)



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
        return n*factorial(n-1)

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
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op
    
def simp():
    print("heloo")


buttons = [
    ('7', lambda: button_click(7)),
    ('8', lambda: button_click(8)),
    ('9', lambda: button_click(9)),
    ('/', lambda: button_click('/')),
    ('4', lambda: button_click(4)),
    ('5', lambda: button_click(5)),
    ('6', lambda: button_click(6)),
    ('*', lambda: button_click('*')),
    ('1', lambda: button_click(1)),
    ('2', lambda: button_click(2)),
    ('3', lambda: button_click(3)),
    ('-', lambda: button_click('-')),
    ('0', lambda: button_click(0)),
    ('.', lambda: button_click('.')),
    ('=', button_equal),
    ('+', lambda: button_click('+')),
    ('!', fact_func),
    ('sin', trig_sin),
    ('cos', trig_cos),
    ('tan', trig_tan),
    ('cot', trig_cot),
    ('√', square_root),
    ('3√', third_root),
    ('+/-', sign_change),
    ('%', percent),
    ('',simp),
    ('DEL', button_delete),
    ('AC', button_clear_all),
    
]

row = 1
col = 0

button_width = 3
button_height = 2

for btn_text, command in buttons:
    if btn_text.isdigit():
        bg_color = "#666666"
        fg_color = "orange"
    else:
        bg_color = "#666666"
        fg_color = "white"
        
    tk.Button(root, text=btn_text, font=('Arial', 16), padx=10, pady=10, command=command, bg=bg_color, fg=fg_color, bd=0, width=button_width, height=button_height).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
