import tkinter as tk

current_expression = ""

def append_to_expression(character):
    global current_expression
    current_expression += str(character)
    display_expression()

def display_expression():
    entry_field.delete(1.0, "end")
    entry_field.insert(1.0, current_expression)

def compute_result():
    global current_expression
    try:
        result = str(eval(current_expression))
        current_expression = result
        display_expression()
    except Exception:
        clear_expression()
        entry_field.insert(1.0, "Error")

def clear_expression():
    global current_expression
    current_expression = ""
    display_expression()

app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x300")

entry_field = tk.Text(app, height=2, width=16, font=("Arial", 24))
entry_field.grid(row=0, column=0, columnspan=4)

button_data = [
    ('7', 1, 0, "lightgrey"), ('8', 1, 1, "lightgrey"), ('9', 1, 2, "lightgrey"), ('/', 1, 3, "lightblue"),
    ('4', 2, 0, "lightgrey"), ('5', 2, 1, "lightgrey"), ('6', 2, 2, "lightgrey"), ('*', 2, 3, "lightblue"),
    ('1', 3, 0, "lightgrey"), ('2', 3, 1, "lightgrey"), ('3', 3, 2, "lightgrey"), ('-', 3, 3, "lightblue"),
    ('C', 4, 0, "lightcoral"),('0', 4, 1, "lightgrey"), ('.', 4, 2, "lightgrey"), ('+', 4, 3, "lightblue"),
    ('(', 5, 0, "lightblue"), (')', 5, 1, "lightblue"), ('%', 5, 2, "lightblue"), ('=', 5, 3, "orange"),
]

for (text, row, col, color) in button_data:
    action = lambda x=text: append_to_expression(x) if x != 'C' else clear_expression()
    if text == '=':
        action = compute_result
    button = tk.Button(app, text=text, command=action, width=5, font=("Arial", 14), bg=color)
    button.grid(row=row, column=col)

app.mainloop()
