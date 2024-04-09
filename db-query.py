import sqlite3

db_local = 'library.db'

# Use the variable db_local instead of the string 'db_local'
connie = sqlite3.connect(db_local)

c = connie.cursor()


c.execute("""
SELECT * FROM Users
""")

Users_info = c.fetchall()

for Users in Users_info:
    print(Users)

connie.commit()
connie.close()