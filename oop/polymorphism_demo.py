import math

# --- Base Class ---
class Shape:
    """Base class requiring an area method implementation."""
    def area(self):
        """
        Base method for area calculation. Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

# --- Derived Class 1: Method Overriding ---
class Rectangle(Shape):
    """Calculates the area of a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Overrides Shape.area() using formula: length * width."""
        return self.length * self.width

# --- Derived Class 2: Method Overriding ---
class Circle(Shape):
    """Calculates the area of a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides Shape.area() using formula: pi * radius^2."""
        return math.pi * (self.radius ** 2)