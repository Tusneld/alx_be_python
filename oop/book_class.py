class Book:
    """
    Class demonstrating constructors, destructors, and string magic methods.
    """
    def __init__(self, title, author, year):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional logging

    def __del__(self):
        """Destructor: Prints a message upon object deletion."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation for the user (print())."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for developers/debugging (repr())."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Note: The expected output relies on the test script's order.