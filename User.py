import sqlite3
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    # def __str__(self):
    #     return "User(id='%s')" % self.id
    @classmethod
    def find_by_username(self, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}'"
        result = cursor.execute(query)
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
            # print(user.username)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_userid(self, id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = f"SELECT * FROM users WHERE id = '{id}'"
        result = cursor.execute(query)
        row = result.fetchone()
        if row:
            user = User(row[0], row[1], row[2])
            # print(user.username)
        else:
            user = None
        connection.close()
        return user


