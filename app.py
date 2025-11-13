import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My First Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.current_input = "0"
        self.display_var = tk.StringVar()
        self.display_var.set(self.current_input)
        self.operator = None
        self.first_number = None

        self.create_widgets()

    def create_widgets(self):
        # Display
        display = ttk.Entry(
            self.root,
            textvariable=self.display_var,
            font=('Arial', 20),
            justify='right',
            state='readonly'
        )
        display.pack(pady=20, padx=20, fill='x')

        # Button frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # Button layout
        buttons = [
            'C', '⌫', '/', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', '=',
            '0', '.', '', ''
        ]

        row, col = 0, 0
        for button in buttons:
            if button:  # Only create button if not empty
                cmd = lambda x=button: self.button_click(x)

                # Style equals button differently
                if button == '=':
                    btn = ttk.Button(button_frame, text=button, command=cmd, style='Accent.TButton')
                else:
                    btn = ttk.Button(button_frame, text=button, command=cmd)

                btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Make buttons expand properly
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value.isdigit() or value == '.':
            self.input_number(value)
        elif value in ['+', '-', '*', '/']:
            self.input_operator(value)
        elif value == '=':
            self.calculate()
        elif value == 'C':
            self.clear()
        elif value == '⌫':
            self.backspace()

    def input_number(self, num):
        if self.current_input == "0":
            self.current_input = num
        else:
            self.current_input += num
        self.display_var.set(self.current_input)

    def input_operator(self, op):
        if self.first_number is None:
            self.first_number = float(self.current_input)
            self.operator = op
            self.current_input = "0"

    def calculate(self):
        if self.first_number is not None and self.operator is not None:
            second_number = float(self.current_input)

            if self.operator == '+':
                result = self.first_number + second_number
            elif self.operator == '-':
                result = self.first_number - second_number
            elif self.operator == '*':
                result = self.first_number * second_number
            elif self.operator == '/':
                if second_number != 0:
                    result = self.first_number / second_number
                else:
                    result = "Error"

            # Handle decimal results
            if result != "Error" and result == int(result):
                result = int(result)

            self.display_var.set(str(result))
            self.current_input = str(result)
            self.first_number = None
            self.operator = None

    def clear(self):
        self.current_input = "0"
        self.display_var.set(self.current_input)
        self.first_number = None
        self.operator = None

    def backspace(self):
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        self.display_var.set(self.current_input)

# Create and run the app
root = tk.Tk()

# Create a style for the equals button
style = ttk.Style()
style.configure('Accent.TButton', foreground='white', background='#0078D7')

app = Calculator(root)
root.mainloop()
