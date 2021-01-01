import sqlite3
from flask_restful import Resource, Api, reqparse


class UserRegister(Resource):
    def post(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str,
                            required=True, help='Username Required')
        parser.add_argument("password", type=str,
                            required=True, help="Password Required")
        data = parser.parse_args()
        find_user = User.find_by_username(data['username'])
        if find_user:
            return {"Message": "Username taken"}, 400
        
        query = f"INSERT INTO users VALUES(NULL, ?,?)"

        password_hash = bcrypt.generate_password_hash(
            data['password']).decode("utf-8")

        cursor.execute(query, (data['username'], password_hash))
        connection.commit()
        connection.close()
        return {"msg": "User Created"}