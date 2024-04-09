import sqlite3

db_local = 'library.db'

# Use the variable db_local instead of the string 'db_local'
connie = sqlite3.connect(db_local)

c = connie.cursor()

# Removed the trailing comma after the last column definition
c.execute("""
    CREATE TABLE Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL UNIQUE,
        Password VARCHAR(255) NOT NULL,
        UserType VARCHAR(50) NOT NULL
    )
""")

connie.commit()
connie.close()
