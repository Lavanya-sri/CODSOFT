import tkinter as tk
import math
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            'Clear']
        row = 1
        col = 0
        for button_text in buttons:
            tk.Button(self.root, text=button_text, padx=20, pady=20, command=lambda text=button_text: self.button_click(text)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def button_click(self, text):
        if text == "=":
            try:
                expression = self.entry.get()
                result = str(eval(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "sqrt":
            try:
                value = float(self.entry.get())
                result = math.sqrt(value)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text in ['sin', 'cos', 'tan']:
            try:
                value = self.entry.get()
                if value:
                    value = float(value)
                    if text == 'sin':
                        result = math.sin(math.radians(value))
                    elif text == 'cos':
                        result = math.cos(math.radians(value))
                    elif text == 'tan':
                        result = math.tan(math.radians(value))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, result)
                else:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Error")
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "Clear":
            self.entry.delete(0, tk.END)
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
