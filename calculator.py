import importlib
import os

# Function to dynamically load plugins from the 'plugins' directory
def load_plugins():
    plugins = {}
    plugin_folder = "plugins"
    
    # Iterate over all files in the 'plugins' folder
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Strip the .py extension to get the module name
            module = importlib.import_module(f"plugins.{module_name}")
            
            # Capitalize the command name and instantiate the class (e.g., AddCommand)
            command_class = getattr(module, f"{module_name.capitalize()}Command")
            plugins[module_name] = command_class()  # Create an instance of the class
    
    return plugins

# The REPL loop for the interactive calculator
def repl():
    commands = load_plugins()  # Load commands dynamically
    
    while True:
        cmd_input = input("Enter command (or 'menu' for available commands, 'exit' to quit): ").lower()

        if cmd_input == "exit":
            print("Exiting calculator...")
            break
        
        # Handle the special 'menu' command
        if cmd_input == "menu":
            print("Available commands:", ", ".join(commands.keys()))
            continue  # Go back to the start of the loop
        
        if cmd_input in commands:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                # Execute the selected command
                result = commands[cmd_input].execute(x, y)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print(f"Unknown command: {cmd_input}")

# Run the REPL loop when the program is executed
if __name__ == "__main__":
    repl()

