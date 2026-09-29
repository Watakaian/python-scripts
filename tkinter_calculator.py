import math
import tkinter as tk
from tkinter import messagebox

# main app window
window = tk.Tk()
window.title("Simple Scientific Calculator")
window.geometry("350x620")


def add_numbers():
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        result = val1 + val2
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def subtract_numbers():
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        result = val1 - val2
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def multiply_numbers():
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        result = val1 * val2
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def divide_numbers():
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        if val2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
        else:
            result = val1 / val2
            label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def square_root():
    try:
        val1 = float(entry_num1.get())
        if val1 < 0:
            messagebox.showerror("Error", "Cannot do square root of negative number!")
        else:
            result = math.sqrt(val1)
            label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter a valid number in Number 1!")

def power_of():
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        result = math.pow(val1, val2)
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

def sin_func():
    try:
        val1 = float(entry_num1.get())
        radians = math.radians(val1)
        result = math.sin(radians)
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter a valid number in Number 1!")

def cos_func():
    try:
        val1 = float(entry_num1.get())
        radians = math.radians(val1)
        result = math.cos(radians)
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter a valid number in Number 1!")

def tan_func():
    try:
        val1 = float(entry_num1.get())
        radians = math.radians(val1)
        result = math.tan(radians)
        label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter a valid number in Number 1!")

def log_func():
    try:
        val1 = float(entry_num1.get())
        if val1 <= 0:
            messagebox.showerror("Error", "Logarithm number must be greater than 0!")
        else:
            result = math.log10(val1)
            label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter a valid number in Number 1!")

def factorial_func():
    try:
        val1 = float(entry_num1.get())
        if val1 < 0 or val1 != int(val1):
            messagebox.showerror("Error", "Factorial needs a whole positive number!")
        else:
            result = math.factorial(int(val1))
            label_result.config(text=f"Result: {result}")
    except:
        messagebox.showerror("Error", "Please enter a valid whole number in Number 1!")

def clear_fields():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")


#interfasce

# App Title
title = tk.Label(window, text="My Calculator", font=("Arial", 16))
title.pack(pady=10)

# no. 1 input
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack(pady=5)

# no. 2 input
label_num2 = tk.Label(window, text="Number 2 (Optional for single operations):")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack(pady=5)

# results
label_result = tk.Label(window, text="Result: ", font=("Arial", 12), fg="blue")
label_result.pack(pady=10)

# buttons

btn_add = tk.Button(window, text="Add (+)", width=20, command=add_numbers)
btn_add.pack(pady=2)

btn_sub = tk.Button(window, text="Subtract (-)", width=20, command=subtract_numbers)
btn_sub.pack(pady=2)

btn_mul = tk.Button(window, text="Multiply (*)", width=20, command=multiply_numbers)
btn_mul.pack(pady=2)

btn_div = tk.Button(window, text="Divide (/)", width=20, command=divide_numbers)
btn_div.pack(pady=2)

btn_sqrt = tk.Button(window, text="Square Root (√)", width=20, command=square_root)
btn_sqrt.pack(pady=2)

btn_pow = tk.Button(window, text="Power (Num1 ^ Num2)", width=20, command=power_of)
btn_pow.pack(pady=2)

btn_sin = tk.Button(window, text="Sin", width=20, command=sin_func)
btn_sin.pack(pady=2)

btn_cos = tk.Button(window, text="Cos", width=20, command=cos_func)
btn_cos.pack(pady=2)

btn_tan = tk.Button(window, text="Tan", width=20, command=tan_func)
btn_tan.pack(pady=2)

btn_log = tk.Button(window, text="Log (base 10)", width=20, command=log_func)
btn_log.pack(pady=2)

btn_fact = tk.Button(window, text="Factorial (x!)", width=20, command=factorial_func)
btn_fact.pack(pady=2)

btn_clear = tk.Button(window, text="Clear All", width=20, bg="red", fg="white", command=clear_fields)
btn_clear.pack(pady=10)

# run the app window
window.mainloop()
