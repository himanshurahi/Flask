from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
from User import User
from flask_bcrypt import Bcrypt
from item import Itemlist, Item

app = Flask(__name__)
app.secret_key = 'rahi'
api = Api(app)

bcrypt = Bcrypt(app)


jwt = JWT(app, authenticate, identity)





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


api.add_resource(Item, "/item/<name>")
api.add_resource(Itemlist, "/items")
api.add_resource(UserRegister, "/register")
# api.add_resource(Student, "/student/<name>")


app.run(port=5001, debug=True)
