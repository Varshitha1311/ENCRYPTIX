from tkinter import *
from tkinter import ttk
import random

def generate_password():
    global password_var
    password_var.set("")  
    password = ""
    length = int(length_entry.get())
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()-=_+,./?><;:"[]\\|}{'
    all_chars = lower_case + upper_case + digits + special_chars
    
    if strength_combobox.get() == 'Low Strength':
        for _ in range(length):
            password += random.choice(lower_case)
    elif strength_combobox.get() == 'Medium Strength':
        for _ in range(length):
            password += random.choice(lower_case + upper_case)
    elif strength_combobox.get() == 'High Strength':
        for _ in range(length):
            password += random.choice(all_chars)
    
    password_var.set(password)

root = Tk()
root.title("Password Generator")
root.geometry("600x400")
root.config(bg="#e0f7fa")

password_var = StringVar(root)

title_label = Label(root, text="Secure Password Generator", font=("Arial", 24, "bold"), fg="#00796b", bg="#e0f7fa")
title_label.pack(pady=20)

password_label = Label(root, text="Password:", font=("Arial", 14), bg="#e0f7fa")
password_label.place(x=100, y=250)
password_entry = Entry(root, font=("Arial", 14), textvariable=password_var, width=25)
password_entry.place(x=200, y=250)

length_label = Label(root, text="Length:", font=("Arial", 14), bg="#e0f7fa")
length_label.place(x=100, y=90)
length_entry = Entry(root, font=("Arial", 14), width=10)
length_entry.place(x=175, y=90)

strength_label = Label(root, text="Strength:", font=("Arial", 14), bg="#e0f7fa")
strength_label.place(x=100, y=150)
strength_combobox = ttk.Combobox(root, font=("Arial", 14), width=15)
strength_combobox['values'] = ('Low Strength', 'Medium Strength', 'High Strength')
strength_combobox.current(1)
strength_combobox.place(x=190, y=150)

generate_button = Button(root, text="Generate", font=("Arial", 14, "bold"), fg="white", bg="#00796b", command=generate_password)
generate_button.place(x=250, y=200)

root.mainloop()
