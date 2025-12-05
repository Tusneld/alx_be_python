# --- Inheritance: Base Class ---
class Book:
    """Base class for all books."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_details(self):
        """Returns basic book details."""
        return f"Book: {self.title} by {self.author}"

#  Add __str__ for general book representation
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    # This method is used by Library.list_books() for custom output
    def get_details(self):
        """Returns basic book details."""
        return f"Book: {self.title} by {self.author}"

# --- Inheritance: Derived Classes ---
class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size
    # Override __str__ for EBook
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
   
    def get_details(self):
        """Overrides base method to include file size."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Derived class for physical printed books."""
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    #  Override __str__ for PrintBook
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
        
    def get_details(self):
        """Overrides base method to include page count."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# --- Composition: Library Class ---
class Library:
    """Class demonstrating composition by managing a collection of books."""
    def __init__(self):
        # The 'books' attribute holds Book/EBook/PrintBook instances (composition)
        self.books = [] 

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only Book objects (or subclasses) can be added.")

    def list_books(self):
        """Prints details of each book in the library using polymorphism."""
        for book in self.books:
            # Polymorphism: calls the correct get_details() method for each object type

            print(book.get_details())
