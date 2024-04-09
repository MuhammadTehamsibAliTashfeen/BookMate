import sqlite3

connie = sqlite3.connect('library.db')

c = connie.cursor()

connie.commit()
connie.close()
