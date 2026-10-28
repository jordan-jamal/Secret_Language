import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    @staticmethod
    def add(x: int, y: int) -> int:
        """Returns the sum of two integers."""
        return x + y

    @staticmethod
    def subtract(x: int, y: int) -> int:
        """Returns the difference of two integers."""
        return x - y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        """Returns the product of two integers."""
        return x * y

    @staticmethod
    def divide(x: int, y: int) -> float:
        """Returns the quotient of two integers, raises ValueError on division by zero."""
        if y == 0:
            logging.error("Division by zero attempted")
            raise ValueError("Cannot divide by zero")
        return x / y

    @staticmethod
    def integer_input(prompt: str) -> int:
        """Prompts the user for an integer input and validates it."""
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                logging.warning("Invalid input, please enter an integer.")
                print("Invalid input. Please enter a valid integer.")

    @staticmethod
    def main():
        """Main method to run the calculator operations."""
        logging.info("Calculator started")
        user_name = input("Enter Your Name: ")
        print(f"So {user_name}, you want a calculator!! \nHere we go!!")

        first_integer = Calculator.integer_input("Enter first Integer: ")
        second_integer = Calculator.integer_input("Enter second Integer: ")

        print(f"The addition of {first_integer} and {second_integer} is {Calculator.add(first_integer, second_integer)}")
        print(f"The subtraction of {first_integer} and {second_integer} is {Calculator.subtract(first_integer, second_integer)}")
        print(f"The multiplication of {first_integer} and {second_integer} is {Calculator.multiply(first_integer, second_integer)}")
        print(f"The division of {first_integer} and {second_integer} is {Calculator.divide(first_integer, second_integer)}")

if __name__ == '__main__':
    Calculator.main()