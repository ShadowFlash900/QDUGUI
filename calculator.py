import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.current_input = ""
        self.result_var = tk.StringVar()
        
        self.create_ui()
    
    def create_ui(self):
        # Дисплей
        display_frame = tk.Frame(self.root, height=100, bg="#f0f0f0")
        display_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.result_var.set("0")
        display = tk.Label(
            display_frame, 
            textvariable=self.result_var, 
            font=("Arial", 24), 
            bg="#f0f0f0", 
            anchor="e", 
            padx=10
        )
        display.pack(fill=tk.BOTH, expand=True)
        
        # Кнопки
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 4)  # Кнопка "=" занимает 4 колонки
        ]
        
        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            colspan = button[3] if len(button) > 3 else 1
            
            btn = tk.Button(
                buttons_frame, 
                text=text, 
                font=("Arial", 18), 
                command=lambda t=text: self.on_button_click(t),
                height=1, 
                width=4 if colspan == 1 else 10
            )
            btn.grid(
                row=row, 
                column=col, 
                columnspan=colspan, 
                padx=2, 
                pady=2, 
                sticky="nsew"
            )
        
        # Настройка размера кнопок
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)
        buttons_frame.grid_rowconfigure(4, weight=1)
    
    def on_button_click(self, text):
        if text == "C":
            self.current_input = ""
            self.result_var.set("0")
        elif text == "=":
            try:
                result = str(eval(self.current_input))
                self.result_var.set(result)
                self.current_input = result
            except Exception:
                messagebox.showerror("Ошибка", "Некорректное выражение")
                self.current_input = ""
                self.result_var.set("0")
        else:
            if self.current_input == "0" and text not in ["+", "-", "*", "/"]:
                self.current_input = text
            else:
                self.current_input += text
            self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
