"""
0. Arithmetic Operations Function
Objective: Define a function that performs basic arithmetic operations to be imported 
           and used in a separate main.py script.
"""

def perform_operation(num1, num2, operation):
    """
    Performs one of four basic arithmetic operations: add, subtract, multiply, or divide.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation, or an error message for division by zero.
    """
    # Use conditional statements (if/elif/else) to determine the operation
    if operation == 'add':
        # Perform addition
        return num1 + num2
    elif operation == 'subtract':
        # Perform subtraction
        return num1 - num2
    elif operation == 'multiply':
        # Perform multiplication
        return num1 * num2
    elif operation == 'divide':
      # Handle the division by zero case as required
        if num2 == 0:
            return "Division by zero is not possible."
        # Perform division
        return num1 / num2
    else:
        # Handle invalid operation input
        return f"Error: Invalid operation '{operation}' specified."


# Note: The provided main.py will import and test this function.
