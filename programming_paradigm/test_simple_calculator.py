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
    def test_addition_positive(self):
        """Test addition with two positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8, "Should be 8")

    def test_addition_negative(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8, "Should be -8")

    def test_addition_mixed(self):
        """Test addition with a positive and a negative number."""
        self.assertEqual(self.calc.add(-5, 5), 0, "Should be 0")
        self.assertEqual(self.calc.add(10, -3), 7, "Should be 7")
        
    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0, 
                               msg="Should be 4.0 and handle floats")

    # --- Test Cases for subtract() ---
    def test_subtraction_positive(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtraction_negative_result(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(5, 12), -7)
        
    # --- Test Cases for multiply() ---
    def test_multiplication_basic(self):
        """Test basic multiplication."""
        self.assertEqual(self.calc.multiply(6, 7), 42)

    def test_multiplication_zero(self):
        """Test multiplication by zero (edge case)."""
        self.assertEqual(self.calc.multiply(100, 0), 0)

    # --- Test Cases for divide() ---
    def test_division_basic(self):
        """Test normal division."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_division_float_result(self):
        """Test division resulting in a float."""
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333333333335)

    def test_division_by_zero(self):
        """Test division by zero (edge case)."""
        # The provided SimpleCalculator returns None for division by zero
        self.assertIsNone(self.calc.divide(10, 0), 
                          "Should return None for division by zero")

# To run tests: python -m unittest test_simple_calculator.py
# The tests will automatically be discovered and executed when run this way.