-- SQL script for performing CRUD operations on the CS 665 Project database

-- Create Operation (Insert a new user)
INSERT INTO Users (UserID, Name, Email, Password, UserType) VALUES
(5, 'Eva Green', 'eva.green@example.com', 'password111', 'Member');

-- Read Operation (Select all books)
SELECT * FROM Books;

-- Update Operation (Update a book's status)
UPDATE Books SET Status = 'Borrowed' WHERE BookID = 2;

-- Delete Operation (Delete a user)
DELETE FROM Users WHERE UserID = 4;

-- Additional Operation: Join Books and Borrowing to see which books are borrowed and by whom
SELECT Books.Title, Books.Author, Users.Name
FROM Books
JOIN Borrowing ON Books.BookID = Borrowing.BookID
JOIN Users ON Borrowing.UserID = Users.UserID;

