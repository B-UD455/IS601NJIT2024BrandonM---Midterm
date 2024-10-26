# Calculator Project for Midterm

## Overview
This project implements a command-line calculator with a REPL interface and a plugin system, utilizing design patterns for scalability and flexibility.

## Design Patterns
This project uses the following design patterns:

- **Command Pattern**: This pattern is used to structure commands within the REPL interface, allowing for a clean separation between user inputs and their execution.
  - [View the implementation here](link_to_command_pattern_file_or_class) (e.g., `repl.py`)
  - Example:
    ```python
    class AddCommand(Command):
        def execute(self, *args):
            return sum(args)
    ```

- **Singleton Pattern**: Ensures that only one instance of the `Logger` class exists, providing centralized logging throughout the application.
  - [View the implementation here](link_to_singleton_class) (e.g., `logger.py`)
    ```python
    class Logger:
        _instance = None
        
        @staticmethod
        def get_instance():
            if Logger._instance is None:
                Logger()
            return Logger._instance
    ```

- **Facade Pattern**: Provides a simplified interface for managing calculation history with Pandas.
  - [View the implementation here](link_to_facade_pattern_file_or_class) (e.g., `history_manager.py`)

## Environment Variables
Environment variables are used to configure the logging level and file paths dynamically. This allows users to adjust configurations without changing the codebase.

- **Example Usage**: The `LOG_LEVEL` variable sets the logging level for the application.
- Code Reference: [Link to environment variable setup](link_to_code_handling_env_vars) (e.g., `config.py`)
  ```python
  import os
  
  LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


## Logging
The application uses Python's `logging` module to track events and errors during execution. Logs are categorized into different levels (INFO, WARNING, ERROR) and can be configured using environment variables.

- **Logging Configuration**: [View the logging setup here](link_to_logging_setup) (e.g., `logger.py`)
  ```python
  import logging
  import os
  
  logging.basicConfig(
      level=os.getenv('LOG_LEVEL', 'INFO'),
      format='%(asctime)s - %(levelname)s - %(message)s'
  )

## Exception Handling: LBYL and EAFP
The project demonstrates both the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches for error handling.

- **LBYL Approach**: This approach checks for conditions before performing operations.
  - Code Reference: [Link to LBYL code example](link_to_lbyl_example) (e.g., `config_manager.py`)
  - Example:
    ```python
    if os.path.exists('config.json'):
        with open('config.json') as file:
            config = json.load(file)
    else:
        print("Configuration file not found.")
    ```

- **EAFP Approach**: This approach attempts to perform an operation directly and handles exceptions if they occur.
  - Code Reference: [Link to EAFP code example](link_to_eafp_example) (e.g., `config_manager.py`)
  - Example:
    ```python
    try:
        with open('config.json') as file:
            config = json.load(file)
    except FileNotFoundError:
        print("Configuration file not found.")
    ```
## Video Demonstration
A video demonstration showcasing the key features of the calculator is available https://youtu.be/qltEplzWVNo

## Setup Instructions
To set up this project on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git
   cd YourRepoName
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables** (optional):
   ```bash
   export LOG_LEVEL=INFO
   ```

4. **Run the REPL interface**:
   ```bash
   python repl.py
   ```

## Usage Examples
- To add two numbers in the REPL, type:

## Testing and Continuous Integration
- **Testing**: The project uses `pytest` for testing and achieves over 90% test coverage.
- To run tests locally, use:
  ```bash
  pytest --cov=your_module_name
