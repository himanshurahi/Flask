import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()
# create_table = "CREATE TABLE items (id INTEGER PRIMARY KEY, name text, price real)"
# cursor.execute(create_table)

# # user = (1, "himanshurahi", "1234")
insert_query = "INSERT INTO items VALUES (null,'book',23)"
cursor.execute(insert_query)

connection.commit()
connection.close()

# select_query = "SELECT * FROM users"

# result = cursor.execute(select_query)
# for res in result:
#     print(res)