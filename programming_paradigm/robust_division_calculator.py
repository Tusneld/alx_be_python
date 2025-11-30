"""
1. Robust Division Calculator with Command Line Arguments
Objective: Implement a division calculator that robustly handles division by zero 
           and non-numeric inputs using try-except blocks.
"""

def safe_divide(numerator: str, denominator: str) -> str:
    """
    Performs division safely, handling ZeroDivisionError and ValueError.

    :param numerator: The numerator as a string (from command line).
    :param denominator: The denominator as a string (from command line).
    :return: A string with the result or an appropriate error message.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den

        # Return the result for successful division
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Catch the specific error for division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Catch the specific error if float conversion failed (non-numeric input)
        return "Error: Please enter numeric values only."

# Note: The provided main.py script will import and test this function
# using sys.argv (command line arguments).