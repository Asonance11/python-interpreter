import ast
import builtins
from io import StringIO
from contextlib import redirect_stdout

class PythonInterpreter:
    def __init__(self, update_output_callback):
        self.update_output_callback = update_output_callback

    def safe_eval(self, code):
        try:
            parsed_code = ast.parse(code, mode='exec')
            compiled_code = compile(parsed_code, filename='<string>', mode='exec')

            with StringIO() as output_buffer:
                with redirect_stdout(output_buffer):
                    exec(compiled_code, {}, builtins.__dict__)

                output_text = output_buffer.getvalue()
                self.update_output_callback(output_text)
        except Exception as e:
            raise ValueError(f"Error: {e}")
