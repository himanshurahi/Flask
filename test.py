import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()
# create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)

# user = (1, "himanshurahi", "1234")
insert_query = "INSERT INTO users VALUES (null,'raja','1234')"
cursor.execute(insert_query)

connection.commit()
connection.close()

# select_query = "SELECT * FROM users"

# result = cursor.execute(select_query)
# for res in result:
#     print(res)