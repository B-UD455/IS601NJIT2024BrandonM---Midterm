from calculator.core import Calculator

class BasicOperationsPlugin:
    def __init__(self):
        self.calculator = Calculator()

    def get_commands(self):
        return {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide
        }

    def add(self, a, b):
        return self.calculator.add(a, b)

    def subtract(self, a, b):
        return self.calculator.subtract(a, b)

    def multiply(self, a, b):
        return self.calculator.multiply(a, b)

    def divide(self, a, b):
        return self.calculator.divide(a, b)
