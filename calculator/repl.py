import logging
from calculator.core import Calculator

import os
from dotenv import load_dotenv

load_dotenv()
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'calculator.log')

logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.logger = logging.getLogger('calculator')

    def start(self):
        print("Calculator REPL started. Type 'exit' to quit.")
        while True:
            user_input = input(">>> ").strip().split()
            if user_input[0].lower() == 'exit':
                print("Exiting REPL.")
                break
            self._handle_command(user_input)

    def _handle_command(self, command):
        try:
            action, *args = command
            if action == 'add':
                result = self.calculator.add(float(args[0]), float(args[1]))
                print(f"Result: {result}")
            # Handle other actions similarly...
            self.logger.info(f"Executed {action} with result: {result}")
        except Exception as e:
            self.logger.error(f"Error in command {command}: {e}")
            print("An error occurred.")
            
    def load_plugins(self):
        from calculator.plugins.basic_operations import BasicOperationsPlugin
        plugin = BasicOperationsPlugin()
        self.commands.update(plugin.get_commands())
            
