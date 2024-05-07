from tkinter import *
import math
import tkinter.messagebox
 
root = Tk()
root.title("Sci-Calculator")
root.configure(background = 'pink')
root.resizable(width = True, height = True)
calc = Frame(root)
calc.grid()
 
class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
 
    def numberEnter(self, num):
        self.result=False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
 
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
 
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
 
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
 
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
 
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True
        
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
 
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
 
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
 
    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
 
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)
 
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
 
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)
 
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)
 
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def atanh(self):
        self.result = False
        self.current = math.atanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)
 
    def floor(self):
        self.result = False
        self.current = math.floor(float(txtDisplay.get()))
        self.display(self.current)
 
    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)
 
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
 
    def ceil(self):
        self.result = False
        self.current = math.ceil(float(txtDisplay.get()))
        self.display(self.current)
 
    def abs(self):
        self.result = False
        self.current = math.abs(float(txtDisplay.get()))
        self.display(self.current)
 
    def pow(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

txtDisplay = Entry(calc, font = ('Arial',18,'bold'), bg = 'white', fg = 'black', bd = 30, width = 28, justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4,)
txtDisplay.insert(0,"0")

numberpadd = "123456789"
i = 0
btn = []
for j in range(2,5):
    for k in  range(3):
        btn.append(Button(calc, width = 6, height=1, bg = 'gray',fg = 'black', font = ('Arial',18,'bold'), bd = 4, text = numberpadd[i]))
        btn[i].grid(row = j, column = k, pady = 1)
        btn[i]["command"] = lambda x = numberpadd[i]:added_value.numberEnter(x)
        i += 1
        
btnClear = Button(calc, text = chr(67), width = 6, height=1, bg = 'blue',
                  font = ('Arial',18,'bold'), bd = 4, 
                  command = added_value.Clear_Entry).grid(row = 1, column = 0, pady = 1)

btnAllClear = Button(calc, text = chr(67)+chr(69), width = 6, height=1, bg = 'blue',
                  font = ('Arial',18,'bold'), bd = 4, 
                  command = added_value.All_Clear_Entry).grid(row = 1, column = 1, pady = 1)

btnsq = Button(calc, text="\u221A", width=6,height=1, bg='gray',
               font=('Arial', 20, 'bold'),
               bd=4, command=added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text = "+", width = 6, height=1, bg = 'blue',
                  font = ('Arial',18,'bold'), bd = 4, 
                  command = lambda:added_value.operation("add")).grid(row = 1, column = 3, pady = 1)

btnSub = Button(calc, text = "-", width = 6, height=1, bg = 'blue',
                  font = ('Arial',18,'bold'), bd = 4, 
                  command = lambda:added_value.operation("sub")).grid(row = 2, column = 3, pady = 1)

btnMul = Button(calc, text="x", width=6, height=1,bg='blue',
                font=('Arial', 18, 'bold'),bd=4, 
                command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text="/", width=6,height=1, bg='blue',
                font=('Arial', 18, 'bold'),
                bd=4, command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

btnZero = Button(calc, text = "0", width = 6, height=1, bg = 'blue',
                  fg = 'grey', font = ('Arial',18,'bold'), bd = 4, 
                  command = lambda:added_value.numberEnter("0")).grid(row = 5, column = 0, pady = 1)

btnDot = Button(calc, text = ".", width = 6, height=1, bg = 'blue',
                  font = ('Arial',18,'bold'), bd = 4, 
                  command = lambda:added_value.numberEnter(".")).grid(row = 5, column = 1, pady = 1)

btnPM = Button(calc, text=chr(177), width=6,height=1, bg='blue',
               font=('Arial', 18, 'bold'),
               bd=4, command=added_value.mathPM).grid(row=5, column=2, pady=1)
 
btnEquals = Button(calc, text = "=", width = 6, height=1, bg = 'green',
                  font = ('Arial',18,'bold'), bd = 4, 
                  command = added_value.sum_of_total).grid(row = 5, column = 3, pady = 1)

#Row 1
btnPi = Button(calc, text="pi", width=6,height=1, bg='blue', fg='black',    #####
               font=('Arial', 18, 'bold'),
               bd=4, command=added_value.pi).grid(row=6, column=0, pady=1)

btnsin = Button(calc, text="sin", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.sin).grid(row=6, column=1, pady=1)

btnCos = Button(calc, text="Cos", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.cos).grid(row=6, column=2, pady=1)
 
btntan = Button(calc, text="tan", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.tan).grid(row=6, column=3, pady=1)

#row 2
btn2Pi = Button(calc, text="2pi", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.tau).grid(row=7, column=0, pady=1)

btnasinh = Button(calc, text="asinh", width=6, height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.asinh).grid(row=7, column=1, pady=1)

btnacosh = Button(calc, text="acosh", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.acosh).grid(row=7, column=2, pady=1)

btnatanh = Button(calc, text="atanh", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.atanh).grid(row=7, column=3, pady=1)

#Row 3
btnlog = Button(calc, text="log", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.log).grid(row=8, column=0, pady=1)
 
btnExp = Button(calc, text="exp", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.exp).grid(row=8, column=1, pady=1)
 
btnMod = Button(calc, text="Mod", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=lambda: added_value.operation("mod")).grid(row=8, column=2, pady=1)
 
btnE = Button(calc, text="e", width=6,height=1, bg='blue', fg='black',
              font=('Arial', 18, 'bold'),
              bd=4, command=added_value.e).grid(row=8, column=3, pady=1)

#Row 4
btnabs = Button(calc, text="abs", width=6,height=1, bg='blue', fg='black',
                  font=('Arial', 18, 'bold'),
                  bd=4, command=added_value.abs).grid(row=9, column=0, pady=1)

btnpow = Button(calc, text = "pow", width = 6, height =1, bg = 'blue',
                  fg = 'black', font = ('Arial',18,'bold'), bd = 4, 
                  command = lambda:added_value.pow).grid(row = 9, column = 1, pady = 1) 

btnfloor = Button(calc, text="floor", width=6,height=1, bg='blue', fg='black',
                  font=('Arial', 18, 'bold'),
                  bd=4, command=added_value.floor).grid(row=9, column=2, pady=1)

btnrcosh = Button(calc, text="cosh", width=6,height=1, bg='blue', fg='black',
                  font=('Arial', 18, 'bold'),
                  bd=4, command=added_value.cosh).grid(row=9, column=3, pady=1)

#Row 5
btnceil = Button(calc, text="ceil", width=6,height=1, bg='blue', fg='black',
                 font=('Arial', 18, 'bold'),
                 bd=4, command=added_value.ceil).grid(row=10, column=0, pady=1)
 
btndeg = Button(calc, text="deg", width=6,height=1, bg='blue', fg='black',
                font=('Arial', 18, 'bold'),
                bd=4, command=added_value.degrees).grid(row=10, column=1, pady=1)

btnradians = Button(calc, text="radians", width=6,height=1, bg='blue', fg='black',
                  font=('Arial', 18, 'bold'),
                  bd=4, command=added_value.radians).grid(row=10, column=2, pady=1)
 
btnsinh = Button(calc, text="sinh", width=6,height=1, bg='blue', fg='black',
                  font=('Arial', 18, 'bold'),
                  bd=4, command=added_value.sinh).grid(row=10, column=3, pady=1) 


 
Calc()

root.mainloop()
