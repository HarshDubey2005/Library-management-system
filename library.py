from book import Book
class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,book):
        self.book.append(book)
        print("Book added succesfully!")
    def remove_book(self,book_id):
        for book in self.book:
            if book.book_id==book_id:
                self.books.remove(book)
                print("Book removed succesfully")
                return
            print(f"No book found with book_id:{book_id}")
    def find_book(self,title):
        for book in self.book:
            if book.title.lower()==title.lower():
                return book
            return None
    def list_books(self):
        if not self.book:
            print("No books available in the library.")
            for book in self.book:
                print(book)