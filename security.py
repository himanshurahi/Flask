from werkzeug.security import safe_str_cmp
import sqlite3
from User import User
from flask_bcrypt import Bcrypt
from flask import Flask, request

app = Flask(__name__)
bcrypt = Bcrypt(app)
# users = [
#     {
#         "id": 1,
#         "username": "himanshurahi",
#         "password": "1234"
#     }
# ]





# users = [
#     User(1, 'himanshurahi', '1234'),
#     User(2, 'user2', 'abcxyz'),
# ]

# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}


# User.find_by_username('himanshurahi')

def authenticate(username, password):
    # user = username_table.get(username, None)
    user = User.find_by_username(username)
    # if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
    #     return user
    if user and bcrypt.check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    # return userid_table.get(user_id, None)
    return User.find_by_userid(user_id)
