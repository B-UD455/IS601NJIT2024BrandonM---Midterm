class BasicOperationsPlugin:
    def get_commands(self):
        return {
            'add': lambda a, b: a + b,
            'subtract': lambda a, b: a - b,
            'multiply': lambda a, b: a * b,
            'divide': lambda a, b: a / b if b != 0 else 'Error: Division by zero.'
        }
