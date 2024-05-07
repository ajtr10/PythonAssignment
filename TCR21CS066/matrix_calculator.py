import tkinter as tk
from tkinter import messagebox
import numpy as np

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.root.configure(bg="#023872")

        self.matrix_entries1 = []
        self.matrix_entries2 = []

        # Create entry widgets for matrix 1 dimensions
        self.label_rows1 = tk.Label(root, text="Matrix 1 Rows:", bg="#023872", fg="white")
        self.label_rows1.grid(row=0, column=0, padx=5, pady=5)
        self.entry_rows1 = tk.Entry(root, bg="#a2e1e8", fg="black")
        self.entry_rows1.grid(row=0, column=1, padx=5, pady=5)

        self.label_cols1 = tk.Label(root, text="Columns:", bg="#023872", fg="white")
        self.label_cols1.grid(row=0, column=2, padx=5, pady=5)
        self.entry_cols1 = tk.Entry(root, bg="#a2e1e8", fg="black")
        self.entry_cols1.grid(row=0, column=3, padx=5, pady=5)

        # Create entry widgets for matrix 2 dimensions
        self.label_rows2 = tk.Label(root, text="Matrix 2 Rows:", bg="#023872", fg="white")
        self.label_rows2.grid(row=1, column=0, padx=5, pady=5)
        self.entry_rows2 = tk.Entry(root, bg="#a2e1e8", fg="black")
        self.entry_rows2.grid(row=1, column=1, padx=5, pady=5)

        self.label_cols2 = tk.Label(root, text="Columns:", bg="#023872", fg="white")
        self.label_cols2.grid(row=1, column=2, padx=5, pady=5)
        self.entry_cols2 = tk.Entry(root, bg="#a2e1e8", fg="black")
        self.entry_cols2.grid(row=1, column=3, padx=5, pady=5)

        # Button to create matrices
        self.create_matrices_button = tk.Button(root, text="Create Matrices", command=self.create_matrices, bg="#2277a6", fg="white")
        self.create_matrices_button.grid(row=1, column=4, padx=5, pady=5)

        # Button to perform operations
        self.add_button = tk.Button(root, text="Add", command=lambda: self.perform_operation('+'), bg="#2277a6", fg="white")
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        self.subtract_button = tk.Button(root, text="Subtract", command=lambda: self.perform_operation('-'), bg="#2277a6", fg="white")
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)
        self.multiply_button = tk.Button(root, text="Multiply", command=lambda: self.perform_operation('*'), bg="#2277a6", fg="white")
        self.multiply_button.grid(row=2, column=2, padx=5, pady=5)

        # Output display
        self.output_text = tk.Text(root, height=10, width=100, bg="#a2e1e8", fg="black")
        self.output_text.grid(row=3, column=0, columnspan=5, pady=5, padx=10)

    def create_matrices(self):
        try:
            rows1 = int(self.entry_rows1.get())
            cols1 = int(self.entry_cols1.get())
            if rows1 <= 0 or cols1 <= 0:
                raise ValueError("Dimensions must be positive integers")

            rows2 = int(self.entry_rows2.get())
            cols2 = int(self.entry_cols2.get())
            if rows2 <= 0 or cols2 <= 0:
                raise ValueError("Dimensions must be positive integers")
        except ValueError as e:
            messagebox.showerror("Error", "Invalid dimensions. Please enter positive integers.")
            return

        # Clear existing matrix entries
        for entry_row in self.matrix_entries1:
            for entry in entry_row:
                entry.destroy()
        self.matrix_entries1 = []
        for entry_row in self.matrix_entries2:
            for entry in entry_row:
                entry.destroy()
        self.matrix_entries2 = []

        # Create entry widgets for matrix 1 elements
        for i in range(rows1):
            entry_row = []
            for j in range(cols1):
                entry = tk.Entry(self.root, width=5, bg="#a2e1e8", fg="black")
                entry.grid(row=i+4, column=j, padx=1, pady=1)
                entry_row.append(entry)
            self.matrix_entries1.append(entry_row)

        # Create entry widgets for matrix 2 elements
        for i in range(rows2):
            entry_row = []
            for j in range(cols2):
                entry = tk.Entry(self.root, width=5, bg="#a2e1e8", fg="black")
                entry.grid(row=i+4, column=j + cols1, padx=1, pady=1)  # Adjust column to align with matrix 1
                entry_row.append(entry)
            self.matrix_entries2.append(entry_row)

    def get_matrices(self):
        try:
            matrix1 = np.array([[float(entry.get()) for entry in row] for row in self.matrix_entries1])
            matrix2 = np.array([[float(entry.get()) for entry in row] for row in self.matrix_entries2])
            return matrix1, matrix2
        except ValueError:
            messagebox.showerror("Error", "Invalid matrix entries. Please enter valid numbers.")
            return None, None

    def perform_operation(self, operation):
        matrix1, matrix2 = self.get_matrices()
        if matrix1 is None or matrix2 is None:
            return

        if operation == '+':
            result = matrix1 + matrix2
            operation_str = "Addition"
        elif operation == '-':
            result = matrix1 - matrix2
            operation_str = "Subtraction"
        elif operation == '*':
            result = np.dot(matrix1, matrix2)
            operation_str = "Multiplication"

        self.display_result(result, operation_str)

    def display_result(self, result, operation_str):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"{operation_str} Result:\n")
        self.output_text.insert(tk.END, np.array2string(result))

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculator(root)
    root.mainloop()
