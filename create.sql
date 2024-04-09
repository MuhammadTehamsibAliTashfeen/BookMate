-- SQL script for creating the database schema for CS 665 Project

-- Users Table
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    UserType VARCHAR(50) NOT NULL,
    -- Functional dependencies: UserID -> {Name, Email, Password, UserType}
    -- Ensuring 3NF by eliminating transitive dependencies and repeating groups.
);

-- Books Table
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(100) NOT NULL,
    ISBN VARCHAR(13) NOT NULL UNIQUE,
    Status VARCHAR(50) NOT NULL,
    -- Functional dependencies: BookID -> {Title, Author, Genre, ISBN, Status}
    -- Ensuring 3NF by eliminating transitive dependencies and repeating groups.
);

-- Borrowing Table
CREATE TABLE Borrowing (
    BorrowID INT PRIMARY KEY,
    UserID INT NOT NULL,
    BookID INT NOT NULL,
    BorrowDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    -- Functional dependencies: BorrowID -> {UserID, BookID, BorrowDate, ReturnDate}
    -- Ensuring 3NF by eliminating transitive dependencies and repeating groups.
);

-- Events Table
CREATE TABLE Events (
    EventID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    Date DATE NOT NULL,
    -- Functional dependencies: EventID -> {Name, Description, Date}
    -- Ensuring 3NF by eliminating transitive dependencies and repeating groups.
);

-- Trigger to update the book status upon borrowing
CREATE TRIGGER UpdateBookStatusBorrowing
AFTER INSERT ON Borrowing
FOR EACH ROW
BEGIN
    UPDATE Books SET Status = 'Borrowed' WHERE BookID = NEW.BookID;
END;

-- Trigger to update the book status upon returning
CREATE TRIGGER UpdateBookStatusReturning
AFTER UPDATE ON Borrowing
FOR EACH ROW WHEN NEW.ReturnDate IS NOT NULL
BEGIN
    UPDATE Books SET Status = 'Available' WHERE BookID = NEW.BookID;
END;

