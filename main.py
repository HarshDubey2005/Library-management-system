from book import Book
from library import Library
from member import Member

def main():
    library=Library()
    member1=Member("Harsh Dubey")
    member2=Member("Rashmi Joshi")

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "1234567891")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "1234567892")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("\nList of all books in the library:")
    library.list_books()

    print("\nBorrowing books:")
    member1.borrow_book(book1)
    member2.borrow_book(book2)
    member2.borrow_book(book1)

    print("\nBooks borrowed by Harsh Dubey:")
    member1.list_borrowed_books()
    print("\nBooks borrowed by Rashmi joshi:")
    member2.list_borrowed_books()

    print("\nReturning books:")
    member1.return_book(book1)
    member1.return_book(book2)

    print("\nList of all books in the library after return:")
    library.list_books()

main()