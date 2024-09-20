The Library Management System is a simple yet effective Python application designed to manage book records and handle member borrowing and returning activities. This project showcases my understanding of object-oriented programming (OOP), handling real-world problems like book availability, and member tracking.

This system is ideal for small libraries or educational institutions that want to automate their day-to-day operations.

Features
Book Management:
Add, remove, and list books in the library.
Track the availability of books (whether a book is borrowed or available).
Member Management:
Library members can borrow and return books.
Ensure that only available books can be borrowed and update availability once returned.
Borrowing History:
Members can view which books they have borrowed at any time.
Project Structure
bash
Copy code
├── book.py           # Contains the Book class for handling book-related operations.
├── library.py        # Defines the Library class that manages the collection of books.
├── member.py         # Contains the Member class to handle member-specific operations like borrowing and returning books.
├── main.py           # The main file where the system operations are executed.
File Breakdown
book.py:
Defines the Book class with attributes like title, author, ISBN, and availability status.
Methods to borrow and return a book, ensuring correct status updates.
library.py:
Manages the list of books in the library.
Methods to add, remove, find, and list books.
member.py:
Defines the Member class which tracks member details and manages their borrowed books.
Methods to borrow and return books and list borrowed books.
main.py:
The entry point for the program where a library and members are created, and various actions like borrowing, returning, and listing books are demonstrated.
How to Run
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/library-management-system.git
Navigate to the project directory:

bash
Copy code
cd library-management-system
Run the program:

bash
Copy code
python3 main.py
Example Usage
Once you run the project, you will see the following operations:

Add books to the library.
List available books.
Members borrow books, ensuring availability is checked.
Return books and update the library’s book status.
bash
Copy code
Book added successfully!
List of all books in the library:
Title: 1984, Author: George Orwell, ISBN: 1234567891, Status: Available
Borrowing books:
Harsh Dubey borrowed 'The Great Gatsby'.
Sorry, 'The Great Gatsby' is not available.
Returning books:
Harsh Dubey returned 'The Great Gatsby'.
Future Enhancements
Persistent Storage: Integrate a database (e.g., SQLite or MySQL) to store book and member data, making the system more scalable.
Graphical User Interface (GUI): Add a user-friendly interface for easier interaction with the system.
Search by Author/Category: Expand the search functionality to include filtering books by author, genre, or publication year.
Technologies Used
Language: Python
Programming Paradigm: Object-Oriented Programming (OOP)
