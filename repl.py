# repl.py
import os
import importlib
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class Command:
    def execute(self, *args):
        raise NotImplementedError("You must implement the execute method.")

def load_plugins():
    commands = {}
    plugin_dir = 'plugins'
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # Remove .py extension
            module = importlib.import_module(f'{plugin_dir}.{module_name}')
            for attr in dir(module):
                command_class = getattr(module, attr)
                if isinstance(command_class, type) and issubclass(command_class, Command):
                    command_instance = command_class()
                    commands[attr.lower()] = command_instance
    return commands

def main():
    commands = {
        'add': AddCommand(),
        'subtract': SubtractCommand(),
        'multiply': MultiplyCommand(),
        'divide': DivideCommand(),
    }
    
    # Load additional commands from plugins
    commands.update(load_plugins())

    print("Welcome to the interactive calculator!")
    print("Available commands: add, subtract, multiply, divide, exit")
    print("Additional commands may be available via plugins.")

    while True:
        user_input = input("Enter command: ").strip().split()
        if user_input[0] == 'exit':
            break

        command_name = user_input[0].lower()
        args = list(map(float, user_input[1:]))

        if command_name in commands:
            try:
                result = commands[command_name].execute(*args)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

