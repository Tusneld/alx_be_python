class Calculator:
    """
    Class demonstrating the distinction between class methods and static methods.
    """
    # Class Attribute, accessible by the class method via 'cls'
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static Method: Utility function, not needing class or instance access.
        (Does not receive 'self' or 'cls').
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class Method: Bounded to the class, receives the class itself ('cls').
        Can access class attributes like calculation_type.
        """
        # Accessing the class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b