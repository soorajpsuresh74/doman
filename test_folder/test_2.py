class Calculator:
    """
    A simple Calculator class that performs basic arithmetic operations.
    """

    def __init__(self, value=0):
        """
        Initializes the calculator with an initial value.
        
        Args:
            value (int, float): The initial value of the calculator. Defaults to 0.
        """
        self.value = value

    def add(self, number):
        """
        Adds the given number to the current value.
        
        Args:
            number (int, float): The number to be added to the current value.
        
        Returns:
            float: The new value after addition.
        """
        self.value += number
        return self.value

    def subtract(self, number):
        """
        Subtracts the given number from the current value.
        
        Args:
            number (int, float): The number to be subtracted from the current value.
        
        Returns:
            float: The new value after subtraction.
        """
        self.value -= number
        return self.value

    def multiply(self, number):
        """
        Multiplies the current value by the given number.
        
        Args:
            number (int, float): The number to multiply the current value by.
        
        Returns:
            float: The new value after multiplication.
        """
        self.value *= number
        return self.value

    def divide(self, number):
        """
        Divides the current value by the given number.
        
        Args:
            number (int, float): The number to divide the current value by.
        
        Returns:
            float: The new value after division.
        
        Raises:
            ValueError: If an attempt is made to divide by zero.
        """
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= number
        return self.value

    def get_value(self):
        """
        Returns the current value of the calculator.
        
        Returns:
            float: The current value.
        """
        return self.value

# Example usage:
if __name__ == "__main__":
    calc = Calculator(10)
    print("Initial value:", calc.get_value())
    print("After addition:", calc.add(5))
    print("After subtraction:", calc.subtract(3))
    print("After multiplication:", calc.multiply(2))
    print("After division:", calc.divide(4))
