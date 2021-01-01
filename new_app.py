from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
from resources.User import UserRegister
from flask_bcrypt import Bcrypt
from resources.item import Itemlist, Item

app = Flask(__name__)
app.secret_key = 'rahi'
api = Api(app)

bcrypt = Bcrypt(app)


jwt = JWT(app, authenticate, identity)








api.add_resource(Item, "/item/<name>")
api.add_resource(Itemlist, "/items")
api.add_resource(UserRegister, "/register")
# api.add_resource(Student, "/student/<name>")


app.run(port=5001, debug=True)
