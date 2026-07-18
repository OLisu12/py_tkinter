import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

window.title("계산기")
window.geometry("350x450")
window.resizable(width=False, height=False)

first_number = 0
selected_operator = ""
new_number = False

def input_decimal():
    global new_number

    current_text = display_bar.get()

    if new_number:
        display_bar.set("0.")
        new_number = False
    elif "." not in current_text:
        display_bar.set(current_text + ".")

def format_result(number):
    if number.is_integer():
        return str(int(number))

    return str(number)

def calculate():
    global first_number
    global selected_operator
    global new_number

    second_number = float(display_bar.get())

    if selected_operator == "+":
        result = (first_number + second_number)
    elif selected_operator == "-":
        result = (first_number - second_number)
    elif selected_operator == "*":
        result = (first_number * second_number)
    elif selected_operator == "/":
        if second_number == 0:
            messagebox.showerror(
                "ERROR",
                "WRONG WAY"
            )
            return

        result = (first_number / second_number)

    display_bar.set(format_result(result))
    new_number = True

def clear_all():
    global first_number
    global selected_operator
    global new_number

    display_bar.set("0")

    first_number = 0
    selected_operator = ""
    new_number = False

def input_number(number):
    global new_number
    current_text = display_bar.get()

    if current_text == "0" or new_number:
        display_bar.set(number)
        new_number = False
    else:
        display_bar.set(current_text + number)

def select_operator(operator):
    global first_number
    global selected_operator
    global new_number

    first_number = float(display_bar.get())
    selected_operator = operator
    new_number = True

def create_button(text, row, column, command):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        command=command
    )

    button.grid(
        row=row,
        column=column,
        sticky="nsew",
        padx=3,
        pady=3
    )
display_bar = tk.StringVar(value=0)
display = tk.Entry(
    window,
    textvariable=display_bar,
    font=("Arial", 30),
    justify="right"
)

display.pack(
    fill="x",
    padx=10,
    pady=10,
    ipady=15
)

button_frame = tk.Frame(window)
button_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

for row in range(5):
    button_frame.rowconfigure(row, weight=1)

for col in range(4):
    button_frame.columnconfigure(col, weight=1)

create_button("1", 0, 0, lambda: input_number("1"))
create_button("2", 0, 1, lambda: input_number("2"))
create_button("3", 0, 2, lambda: input_number("3"))
create_button("4", 1, 0, lambda: input_number("4"))
create_button("5", 1, 1, lambda: input_number("5"))
create_button("6", 1, 2, lambda: input_number("6"))
create_button("7", 2, 0, lambda: input_number("7"))
create_button("8", 2, 1, lambda: input_number("8"))
create_button("9", 2, 2, lambda: input_number("9"))
create_button("0", 3, 1, lambda: input_number("0"))
create_button("=", 3, 2, lambda: calculate())
create_button("C", 3, 0, lambda: clear_all())
create_button(".", 4, 2, lambda: input_decimal())
create_button("", 4, 0, lambda: None)
create_button("", 4, 1, lambda: None)
create_button("", 4, 3, lambda: None)

create_button(
    "+",
    3,
    3,
    lambda: select_operator("+")
)

create_button(
    "-",
    2,
    3,
    lambda: select_operator("-")
)

create_button(
    "x",
    1,
    3,
    lambda: select_operator("*")
)

create_button(
    "/",
    0,
    3,
    lambda: select_operator("/")
)
window.mainloop()