# commands.py
from command import Command

class AddCommand(Command):
    def execute(self, x, y):
        return x + y

class SubtractCommand(Command):
    def execute(self, x, y):
        return x - y

class MultiplyCommand(Command):
    def execute(self, x, y):
        return x * y

class DivideCommand(Command):
    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

