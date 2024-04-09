import sqlite3

db_local = 'library.db'

# Use the variable db_local instead of the string 'db_local'
connie = sqlite3.connect(db_local)

c = connie.cursor()


c.execute("""
INSERT INTO Users (UserID, Name, Email, Password, UserType) VALUES
(1, 'John Doe', 'john.doe@example.com', 'password123', 'Member'),
(2, 'Jane Smith', 'jane.smith@example.com', 'password456', 'Admin'),
(3, 'Alice Johnson', 'alice.johnson@example.com', 'password789', 'Member'),
(4, 'Bob Brown', 'bob.brown@example.com', 'password101', 'Librarian');
""")
connie.commit()
connie.close()

Inserting Books
INSERT INTO Books (BookID, Title, Author, Genre, ISBN, Status) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', '1234567890123', 'Available'),
(2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', '1234567890124', 'Available'),
(3, '1984', 'George Orwell', 'Dystopian', '1234567890125', 'Borrowed'),
(4, 'Pride and Prejudice', 'Jane Austen', 'Romance', '1234567890126', 'Available');

-- Inserting Borrowings
INSERT INTO Borrowing (BorrowID, UserID, BookID, BorrowDate, ReturnDate) VALUES
(1, 3, 3, '2023-01-10', NULL);

-- Inserting Events
INSERT INTO Events (EventID, Name, Description, Date) VALUES
(1, 'Book Club Meeting', 'Monthly book club meeting to discuss our latest read.', '2023-02-15'),
(2, 'Author Visit', 'Meet the Author event with local writer James Carter.', '2023-03-10');

