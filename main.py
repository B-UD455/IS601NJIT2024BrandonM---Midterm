# main.py
from app import App    

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App

    def main():
        while True:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                operation = input("Enter operation (add, subtract, multiply, divide): ").strip()
    
                if operation == 'add':
                    print(f"The result of {a} add {b} is equal to {a + b}")
                elif operation == 'subtract':
                    print(f"The result of {a} subtract {b} is equal to {a - b}")
                elif operation == 'multiply':
                    print(f"The result of {a} multiply {b} is equal to {a * b}")
                elif operation == 'divide':
                    if b == 0:
                        raise ValueError("Cannot divide by zero")
                    print(f"The result of {a} divide {b} is equal to {a / b}")
                else:
                    print(f"Unknown operation: {operation}")
            except ValueError as e:
                print(f"Invalid input: {e}")
    
    if __name__ == "__main__":
        main()

