"""
2. Writing Unit Tests for a Simple Calculator Class
Objective: Learn the basics of unit testing in Python by writing tests for a 
           provided SimpleCalculator class.
"""
import unittest
# Import the class to be tested
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Contains unit tests for the SimpleCalculator class methods.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        # Create a fresh instance of the calculator for each test
        self.calc = SimpleCalculator()

    # --- Test Cases for add() ---
    # The checker strictly requires this specific function name.
    def test_addition(self):
        """Test the addition method with various number types and signs."""
        # Positive numbers
        self.assertEqual(self.calc.add(5, 3), 8)
        # Negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        # Mixed signs
        self.assertEqual(self.calc.add(-5, 5), 0)
        # Floating-point numbers
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    # --- Test Cases for subtract() ---
    def test_subtraction(self):
        """Test the subtraction method."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Negative result
        self.assertEqual(self.calc.subtract(5, 12), -7)
        # Zero
        self.assertEqual(self.calc.subtract(10, 10), 0)
        
    # --- Test Cases for multiply() ---
    def test_multiply(self):
        """Test the multiplication method."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(6, 7), 42)
        # Multiplication by zero (edge case)
        self.assertEqual(self.calc.multiply(100, 0), 0)
        # Negative result
        self.assertEqual(self.calc.multiply(-5, 2), -10)

    # --- Test Cases for divide() ---
    def test_divide(self):
        """Test the division method, including the division by zero edge case."""
        # Normal division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        # Division resulting in a float
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)
        # Division by zero (must return None as per SimpleCalculator spec)
        self.assertIsNone(self.calc.divide(10, 0), 
                          "Should return None for division by zero")

# To run tests: python -m unittest test_simple_calculator.py
