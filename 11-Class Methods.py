class Book:
    # Class variable to keep track of total books
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        """Class method to increment the total book count."""
        cls.total_books += 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Increment total_books every time a new book object is created
        Book.increment_book_count()

# Adding some books to test the class method
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("Moby-Dick", "Herman Melville")

# Display the total count of books
print(f"Total books: {Book.total_books}")
