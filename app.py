import sqlite3

connection = sqlite3.connect("restaurantmenu.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM restaurant")
results = cursor.fetchall()
for r in results:
    print(r)
cursor.close()
connection.close()