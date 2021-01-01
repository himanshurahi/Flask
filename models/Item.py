import sqlite3


class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}

    @classmethod
    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name, ))
        row = result.fetchone()
        connection.close()
        if row:
            # return {"item": {
            #     "name": row[0],
            #     "price": row[1]
            # }}
            return self(row[0], row[1])

        return None

    @classmethod
    def insert_item(self, name, price):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = f"INSERT INTO items VALUES(NULL,?,?)"
        result = cursor.execute(query, (name, price))
        connection.commit()
        connection.close()
        return {"message": "Item Added Successfully"}
