"""
3. Implementing Basic OOP for a Library Management System
Objective: Implement classes to track books in a library, focusing on classes, 
           object instantiation, and method invocation.
"""

class Book:
    """
    Represents a book with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a Book object.

        :param title: The title of the book (public attribute).
        :param author: The author of the book (public attribute).
        """
        self.title = title
        self.author = author
        # Encapsulation: Use a private attribute to track availability
        self._is_checked_out = False 

    def check_out(self) -> bool:
        """Marks the book as checked out if it's currently available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self) -> bool:
        """Marks the book as available if it's currently checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self) -> bool:
        """Returns the current availability status."""
        return not self._is_checked_out
    
    def __str__(self):
        """A string representation of the book object."""
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes the Library with an empty list to store books.
        """
        # Encapsulation: Use a private attribute for the list of books
        self._books = []

    def add_book(self, book: Book):
        """Adds a Book object to the library's collection."""
        self._books.append(book)

    def find_book(self, title: str) -> Book or None:
        """Helper to find a book by title."""
        # Iterate through the list of books to find a match
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title: str) -> bool:
        """
        Attempts to check out a book by title.

        :param title: The title of the book to check out.
        :return: True if successful, False otherwise.
        """
        book = self.find_book(title)
        if book and book.is_available():
            book.check_out()
            return True
        return False

    def return_book(self, title: str) -> bool:
        """
        Attempts to return a book by title.

        :param title: The title of the book to return.
        :return: True if successful, False otherwise.
        """
        book = self.find_book(title)
        if book and not book.is_available():
            book.return_book()
            return True
        return False

    def list_available_books(self):
        """
        Prints the title and author of all books that are currently available.
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book) # Uses the __str__ method of the Book class
                available_found = True
        
        if not available_found:
            print("No books are currently available.")

# Note: The provided main.py script will import and test this class structure.