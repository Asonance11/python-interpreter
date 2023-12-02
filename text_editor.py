import tkinter as tk
from io import StringIO
from contextlib import redirect_stdout
from python_interpreter import PythonInterpreter

class PythonTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")

        # Code Input
        self.code_input = tk.Text(self.root, height=10, width=50)
        self.code_input.pack()

        # Execute Button
        self.execute_button = tk.Button(self.root, text="Run Code", command=self.interpret_code)
        self.execute_button.pack()

        # Output Display
        self.output_text = tk.Text(self.root, height=5, width=50)
        self.output_text.pack()

        # Interpreter
        self.interpreter = PythonInterpreter(self.update_output_text)

    def interpret_code(self):
        source_code = self.code_input.get("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

        try:
            self.interpreter.safe_eval(source_code)
        except ValueError as ve:
            self.output_text.insert(tk.END, str(ve))

    def update_output_text(self, text):
        self.output_text.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonTextEditor(root)
    root.mainloop()
