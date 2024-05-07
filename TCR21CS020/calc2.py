from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

expression = ""


from tkinter import messagebox
matA = None
matB = None
matC = None
matD = None

def evaluate_matrix_operation(expression, result_label):

    matrix_operation = expression.get()
    print("matA in evaluate", matA)


    if matA is not None and 'matA' in matrix_operation:
        matrix_operation = matrix_operation.replace('matA', 'matA')

    if matB is not None and 'matB' in matrix_operation:
        matrix_operation = matrix_operation.replace('matB', 'matB')

    if matC is not None and 'matC' in matrix_operation:
        matrix_operation = matrix_operation.replace('matC', 'matC')

    if matD is not None and 'matD' in matrix_operation:
        matrix_operation = matrix_operation.replace('matD', 'matD')

    try:
        if '+' in matrix_operation:
            result = add_matrices(matrix_operation)
            result_label.config(text=f"The result is:  {result}")
        elif '-' in matrix_operation:
            result = subtract_matrices(matrix_operation)
            result_label.config(text=f"The result is:  {result}")
        elif '*' in matrix_operation:
            result = multiply_matrices(matrix_operation)
            result_label.config(text=f"The result is:  {result}")
        else:
            result_label.config(text="Invalid operation. Please enter a valid matrix operation.")
    except SyntaxError:
        result_label.config(text="Invalid syntax. Please enter a valid matrix operation.")
    except ValueError as ve:
        result_label.config(text=f"Error occurred: {ve}")
    except Exception as e:
        result_label.config(text=f"Error occurred: {e}")

def multiply_matrices(matrix_operation):

    matrices = [eval(mat) for mat in matrix_operation.split('*')]

    if len(matrices[0][0]) != len(matrices[1]):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrices[1])] for row in matrices[0]]
    return result
def subtract_matrices(matrix_operation):

    matrices = [eval(mat) for mat in matrix_operation.split('-')]

    dimensions = set(len(mat) for mat in matrices), set(len(row) for mat in matrices for row in mat)
    if len(dimensions[0]) > 1 or len(dimensions[1]) > 1:
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    result = [[values[0] - sum(values[1:]) for values in zip(row, *other_rows)] for row, *other_rows in zip(*matrices)]
    return result

def add_matrices(matrix_operation):

    matrices = [eval(mat) for mat in matrix_operation.split('+')]

    dimensions = set(len(mat) for mat in matrices), set(len(row) for mat in matrices for row in mat)
    if len(dimensions[0]) > 1 or len(dimensions[1]) > 1:
        raise ValueError("Matrices must have the same dimensions for addition.")

    result = [[sum(values) for values in zip(*rows)] for rows in zip(*matrices)]
    return result





def store_matrix():
    def on_matrix_button_click(matrix_name):
      global current_matrix, current_row, current_col
      current_matrix = matrix_name
      current_row = 0  
      current_col = 0  
      rows_label.config(text=f"Enter number of rows for {matrix_name}:")
      input_entry.delete(0, END)
      input_entry.config(state=NORMAL)  
    def on_digit_click(digit):
        current_value = input_entry.get()
        input_entry.delete(0, END)
        input_entry.insert(END, current_value + digit)



    def on_enter_click():
      global current_row, current_col, current_matrix
      nonlocal current_state, current_rows, current_columns, matrix_values

      
      if 'current_row' not in globals():
          current_row = 0
      if 'current_col' not in globals():
          current_col = 0
      
      if current_state == "rows":
          current_rows = int(input_entry.get())
          input_entry.delete(0, END)
          rows_label.config(text=f"Enter number of columns for {current_matrix}:")
          current_state = "columns"
      elif current_state == "columns":
          current_columns = int(input_entry.get())
          input_entry.delete(0, END)
          matrix_values = [[0 for _ in range(current_columns)] for _ in range(current_rows)]
          current_state = "input"
          rows_label.config(text=f"Enter matrix {current_matrix} values:")
          input_entry.config(state=NORMAL) 
      elif current_state == "input":
          input_value = input_entry.get()
          if input_value:
              matrix_values[current_row][current_col] = int(input_value)
              input_entry.delete(0, END)
              print("Matrix_values:", matrix_values)
              current_col += 1
              if current_col == current_columns:
                  current_col = 0
                  current_row += 1
              if current_row == current_rows and current_col == 0:
                
                input_entry.config(state=DISABLED)  
                store_matrix_value()  
                store_matrix_window.destroy()  
              else:
                input_entry.focus_set() 
          else:
              messagebox.showerror("Error", "Please enter a value.")






    def go_back():
        store_matrix_window.destroy()

    def on_clear_click():
        input_entry.delete(0, END)
    
    def store_matrix_value():
      global matA, matB, matC, matD, current_matrix
      nonlocal matrix_values, current_rows, current_columns

      print("current matrix is", current_matrix)
      if current_matrix == "matA":
         
          matA = matrix_values
            
      elif current_matrix == "matB":
          #global matB
          matB = matrix_values
      elif current_matrix == "matC":
          #global matC
          matC = matrix_values
      elif current_matrix == "matD":
          #global matD
          matD = matrix_values
     
      print("matA is",matA)
      print("Length of matrix_values:", len(matrix_values))
      print("Current rows:", current_rows)
      print("Current columns:", current_columns)
      print("Expected length:", current_rows * current_columns)
      if sum(len(row) for row in matrix_values) == current_rows * current_columns:
    
        messagebox.showinfo("Success", f"{current_matrix} is successfully stored.")
        
        store_matrix_window.destroy()
        #matrix_mode()  
      else:
          messagebox.showerror("Error", "Matrix not fully entered.")

    store_matrix_window = Toplevel()
    store_matrix_window.title("Store Matrices")

    current_matrix = ""
    current_state = "rows"
    current_rows = 0
    current_columns = 0
    matrix_values = []
    
    matrix_buttons_frame = Frame(store_matrix_window)
    matrix_buttons_frame.pack()
    
    matA_button = Button(matrix_buttons_frame, text="matA", padx=10, pady=5, width=5, command=lambda: on_matrix_button_click("matA"))
    matA_button.grid(row=0, column=0, padx=5, pady=5)
    
    matB_button = Button(matrix_buttons_frame, text="matB", padx=10, pady=5, width=5, command=lambda: on_matrix_button_click("matB"))
    matB_button.grid(row=0, column=1, padx=5, pady=5)
    
    matC_button = Button(matrix_buttons_frame, text="matC", padx=10, pady=5, width=5, command=lambda: on_matrix_button_click("matC"))
    matC_button.grid(row=0, column=2, padx=5, pady=5)
    
    matD_button = Button(matrix_buttons_frame, text="matD", padx=10, pady=5, width=5, command=lambda: on_matrix_button_click("matD"))
    matD_button.grid(row=0, column=3, padx=5, pady=5)
    
    input_frame = Frame(store_matrix_window)
    input_frame.pack(pady=10)
    
    rows_label = Label(input_frame, text="Enter number of rows:", padx=5, pady=5)
    rows_label.grid(row=0, column=0)
    
    input_entry = Entry(input_frame, width=10, state=DISABLED)
    input_entry.grid(row=0, column=1, padx=5, pady=5)
    
    buttons_frame = Frame(store_matrix_window)
    buttons_frame.pack()
    
    digit_buttons = []
    for i in range(10):
        digit_buttons.append(Button(buttons_frame, text=str(i), padx=10, pady=5, width=5, command=lambda i=i: on_digit_click(str(i))))
        digit_buttons[i].grid(row=i//3, column=i%3, padx=5, pady=5)
    
    enter_button = Button(buttons_frame, text="Enter", padx=10, pady=5, width=5, command=on_enter_click)
    enter_button.grid(row=4, column=3, padx=5, pady=5)
    
    clear_button = Button(buttons_frame, text="Clear", padx=10, pady=5, width=5, command=on_clear_click)
    clear_button.grid(row=4, column=4, padx=5, pady=5)
    
    back_button = Button(store_matrix_window, text="Back", padx=10, pady=5, width=10, command=go_back)
    back_button.pack(side=BOTTOM, pady=10)
    input_entry.focus_set()






def matrix_mode():
    global matrix_equation
    matrix_window = Toplevel(gui)
    matrix_window.title('Matrix Operations')
    matrix_frame = Frame(master=matrix_window, bg="lightgray", padx=20, pady=10)
    matrix_frame.grid()  
    def matrix_press(num): 
   
      global matrix_equation

      
      matrix_equation.set(matrix_equation.get() + str(num))

    def switch_to_normal_mode():
        matrix_window.destroy()
        expression_field.config(state=tk.NORMAL)
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, "")
        Matrix_Ops.config(command=matrix_mode)


    def add_matrix():      
        pass

    def subtract_matrix():
        pass

    def scalar_multiply_matrix():
        pass

    def multiply_matrix():
        pass

    def transpose_matrix():
        pass

    def inverse_matrix():
        pass

    def determinant_matrix():
        pass
    def clear_expression_field(entry):
      entry.delete(0, END)

    matrix_equation = StringVar() 
    expression_field2 = Entry(matrix_frame, textvariable=matrix_equation) 
    expression_field2.grid(row=0, column=0, columnspan=4, ipadx=70)
    result_label = Label(matrix_frame, text="", font=("Arial", 16), wraplength=300)
    result_label.grid(row=1, column=0)

    button1 = Button(matrix_frame, text=' 1 ', fg='black', bg='red', 
                    command=lambda: matrix_press(1), height=1, width=7) 
    button1.grid(row=2, column=0) 


    button2 = Button(matrix_frame, text=' 2 ', fg='black', bg='red', 
            command=lambda: matrix_press(2), height=1, width=7) 
    button2.grid(row=2, column=1) 

    button3 = Button(matrix_frame, text=' 3 ', fg='black', bg='red', 
            command=lambda: matrix_press(3), height=1, width=7) 
    button3.grid(row=2, column=2) 

    button4 = Button(matrix_frame, text=' 4 ', fg='black', bg='red', 
            command=lambda: matrix_press(4), height=1, width=7) 
    button4.grid(row=3, column=0) 

    button5 = Button(matrix_frame, text=' 5 ', fg='black', bg='red', 
            command=lambda: matrix_press(5), height=1, width=7) 
    button5.grid(row=3, column=1) 

    button6 = Button(matrix_frame, text=' 6 ', fg='black', bg='red', 
            command=lambda: matrix_press(6), height=1, width=7) 
    button6.grid(row=3, column=2) 

    button7 = Button(matrix_frame, text=' 7 ', fg='black', bg='red', 
            command=lambda: matrix_press(7), height=1, width=7) 
    button7.grid(row=4, column=0) 

    button8 = Button(matrix_frame, text=' 8 ', fg='black', bg='red', 
            command=lambda: matrix_press(8), height=1, width=7) 
    button8.grid(row=4, column=1) 

    button9 = Button(matrix_frame, text=' 9 ', fg='black', bg='red', 
            command=lambda: matrix_press(9), height=1, width=7) 
    button9.grid(row=4, column=2) 

    button0 = Button(matrix_frame, text=' 0 ', fg='black', bg='red', 
            command=lambda: matrix_press(0), height=1, width=7) 
    button0.grid(row=5, column=1) 
    button_addition = Button(master=matrix_frame, text="Addition", padx=15, pady=5, width=10, command=lambda:matrix_press('+'))
    button_addition.grid(row=8, column=0, pady=5)

    button_subtraction = Button(master=matrix_frame, text="Subtraction", padx=15, pady=5, width=10, command=lambda:matrix_press('-'))
    button_subtraction.grid(row=8, column=2, pady=5)

    button_scalar_multiply = Button(master=matrix_frame, text="Scalar Multiply", padx=15, pady=5, width=10, command=lambda:matrix_press('*'))
    button_scalar_multiply.grid(row=9, column=0, pady=5)

    button_multiply = Button(master=matrix_frame, text="Multiplication", padx=15, pady=5, width=10, command=lambda:matrix_press('*'))
    button_multiply.grid(row=9, column=2, pady=5)

    button_transpose = Button(master=matrix_frame, text="Transpose", padx=15, pady=5, width=10, command=transpose_matrix)
    button_transpose.grid(row=10, column=0, pady=5)

    button_inverse = Button(master=matrix_frame, text="Inverse", padx=15, pady=5, width=10, command=inverse_matrix)
    button_inverse.grid(row=10, column=2, pady=5)

    button_determinant = Button(master=matrix_frame, text="Determinant", padx=15, pady=5, width=10, command=determinant_matrix)
    button_determinant.grid(row=11, column=0, pady=5)
    store_button = Button(master=matrix_frame, text="Store", padx=15, pady=5, width=10, command=store_matrix)
    store_button.grid(row=11, column=2, columnspan=7, pady=5)
    matA_button = Button(master=matrix_frame, text="matA", padx=15, pady=5, width=10, command=lambda:matrix_press('matA'))
    matA_button.grid(row=12, column=0, pady=5)
    matB_button = Button(master=matrix_frame, text="matB", padx=15, pady=5, width=10, command=lambda:matrix_press('matB'))
    matB_button.grid(row=12, column=2, pady=5)
    matC_button = Button(master=matrix_frame, text="matC", padx=15, pady=5, width=10, command=lambda:matrix_press('matC'))
    matC_button.grid(row=13, column=0, pady=5)
    matD_button = Button(master=matrix_frame, text="matD", padx=15, pady=5, width=10, command=lambda:matrix_press('matD'))
    matD_button.grid(row=13, column=2, pady=5)
    

    button_equal = Button(master=matrix_frame, text="Equal", padx=15, pady=5, width=10, command=lambda: evaluate_matrix_operation(matrix_equation, result_label))
    button_equal.grid(row=14, column=0, pady=10)
    button_clear = Button(master=matrix_frame, text="Clear", padx=15, pady=5, width=10, command=lambda: clear_expression_field(expression_field2))
    button_clear.grid(row=14, column=2, pady=10)
    button_back = Button(master=matrix_frame, text="Back to Calculator", padx=15, pady=5, width=10, command=switch_to_normal_mode)
    button_back.grid(row=15, column=0, pady=10)


def press(num): 

	global expression 
	expression = expression + str(num) 
	equation.set(expression) 



def equalpress(): 

	try: 

		global expression 

		total = str(eval(expression)) 

		equation.set(total) 
		expression = "" 
	except: 

		equation.set(" error ") 
		expression = "" 

def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


if __name__ == "__main__": 

	gui = Tk() 

	gui.title("Simple Calculator") 


	gui.geometry("270x150") 
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation) 
	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
					command=lambda: press(1), height=1, width=7) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
					command=lambda: press(2), height=1, width=7) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
					command=lambda: press(3), height=1, width=7) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
					command=lambda: press(4), height=1, width=7) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
					command=lambda: press(5), height=1, width=7) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
					command=lambda: press(6), height=1, width=7) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
					command=lambda: press(7), height=1, width=7) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
					command=lambda: press(8), height=1, width=7) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
					command=lambda: press(9), height=1, width=7) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
					command=lambda: press(0), height=1, width=7) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='red', 
				command=lambda: press("+"), height=1, width=7) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='red', 
				command=lambda: press("-"), height=1, width=7) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='red', 
					command=lambda: press("*"), height=1, width=7) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='red', 
					command=lambda: press("/"), height=1, width=7) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='red', 
				command=equalpress, height=1, width=7) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1,width=7) 
	clear.grid(row=5, column='1') 

	Decimal= Button(gui, text='.', fg='black', bg='red', 
					command=lambda: press('.'), height=1, width=7) 
	Decimal.grid(row=6, column=0) 
	Matrix_Ops=  Button(gui, text='Matrix Ops', fg='black', bg='red', 
					command=matrix_mode, height=1, width=7)
	Matrix_Ops.grid(row=6, column=1) 

	gui.mainloop() 
