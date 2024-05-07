import tkinter as tk
import math

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
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

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
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def third_root():
    global calc_operator
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '(1/3)'))
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

tk_calc = tk.Tk()
tk_calc.configure(bg="#293C4A", bd=10)
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = tk.StringVar()

text_display = tk.Entry(tk_calc, font=('Arial', 20, 'bold'), textvariable=text_input,
                        bd=5, insertwidth=5, bg='#BBB', justify='right')
text_display.grid(columnspan=5, padx=10, pady=15)

button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('Arial', 16, 'bold')}
button_params_main = {'bd': 5, 'fg': '#000', 'bg': '#BBB', 'font': ('Arial', 16, 'bold')}

buttons = [
    ('abs', button_click), ('mod', button_click), ('div', button_click), ('x!', fact_func), ('e', lambda: button_click(str(math.exp(1)))),
    ('sin', trig_sin), ('cos', trig_cos), ('tan', trig_tan), ('cot', trig_cot), ('π', lambda: button_click(str(math.pi))),
    ('x²', lambda: button_click('*2')), ('x³', lambda: button_click('3')), ('x^n', lambda: button_click('')), ('x⁻¹', lambda: button_click('(-1)')), ('10^x', lambda: button_click('10*')),
    ('√', square_root), ('³√', third_root), ('ⁿ√', lambda: button_click('(1/')), ('log₁₀', lambda: button_click('log(')), ('ln', lambda: button_click('ln(')),
    ('(', lambda: button_click('(')), (')', lambda: button_click(')')), ('±', sign_change), ('%', percent), ('e^x', lambda: button_click('e(')),
    ('7', lambda: button_click('7')), ('8', lambda: button_click('8')), ('9', lambda: button_click('9')), ('DEL', button_delete), ('AC', button_clear_all),
    ('4', lambda: button_click('4')), ('5', lambda: button_click('5')), ('6', lambda: button_click('6')), ('', lambda: button_click('')), ('/', lambda: button_click('/')),
    ('1', lambda: button_click('1')), ('2', lambda: button_click('2')), ('3', lambda: button_click('3')), ('+', lambda: button_click('+')), ('-', lambda: button_click('-')),
    ('0', lambda: button_click('0')), ('.', lambda: button_click('.')), ('EXP', lambda: button_click('10*')), ('=', button_equal)
]

row_counter = 1
col_counter = 0

for (text, command) in buttons:
    button = tk.Button(tk_calc, button_params, text=text, command=command)
    button.grid(row=row_counter, column=col_counter, sticky="nsew")
    col_counter += 1
    if col_counter > 4:
        col_counter = 0
        row_counter += 1

tk_calc.mainloop()
