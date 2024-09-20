class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # This should be True initially, meaning the book is available.

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {availability}"

    def borrow(self):
        if self.available:
            self.available = False  # Mark the book as not available.
            return True
        return False

    def return_book(self):
        self.available = True  # Mark the book as available.
