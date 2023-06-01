import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display calculation result
        self.result_entry = tk.Entry(self.root, width=30, font=('Arial', 14))
        self.result_entry.grid(row=0, column=0, columnspan=4, pady=7)

        # Buttons for numbers and operators
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '%',
        ]
        row = 1
        col = 0
        for button_text in button_texts:
            
            button = tk.Button(self.root, text=button_text, width=5, height=2, font=('Arial', 14), command=lambda text=button_text: self.on_button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, text):
        # Append clicked button's text to result_entry
        current_text = self.result_entry.get()
        if text == '=':
            try:
                # Handle percentage calculation
                result = eval(current_text.replace('%', '*0.01*'))
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, result)
            except Exception as e:
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, 'Error: ' + str(e))
        elif text == 'C':  # handle clear button
            self.result_entry.delete(0, tk.END)
        else:
            self.result_entry.insert(tk.END, text)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()
