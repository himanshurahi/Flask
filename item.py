from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
from User import User
from flask_bcrypt import Bcrypt

items = [{
    "name": "himanshurahi",
    "price": 1
},
    {
    "name": "rahi",
    "price": 100
}]


class Item(Resource):
    def get(self, name):
        # item = next(filter(lambda x: x['name'] == name, items), 'Not Found')
        # print(item)
        # return {'item': item}, 200 if item else 404
        # for item in items:
        #     if(item['name'] == name):
        #         return item
        #     else:
        #         return {"error": "No Item Found"}, 404
        return Item.find_by_name(name)

    def post(self, name):
        requested_data = request.get_json()
        if Item.find_by_name(name) is not None:
            return {"Message": "Item Already Exist"}
        else:
            return Item.insert_item(name, requested_data['price'])

        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # query = f"INSERT INTO items VALUES(NULL,?,?)"
        # result = cursor.execute(query, (name, requested_data['price']))
        # connection.commit()
        # connection.close()
        # return {"message": "Item Added Successfully"}

        # item = next(filter(lambda x: x['name'] == name, items), None)
        # if item is not None:
        #     return {"Error_msg": f"Item {name} already Exist"}

        # item = {"name": name, "price": requested_data['price']}
        # items.append(item)
        # return items

    def delete(self, name):
        # requested_data = request.get_json()
        # myitems = next(filter(lambda x: x['name'] != name, items), None)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = f"DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name, ))
        connection.commit()
        connection.close()

        return {"message": "Item Deleted Successfully."}

    @classmethod
    def find_by_name(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name, ))
        row = result.fetchone()
        connection.close()
        if row:
            return {"item": {
                "name": row[0],
                "price": row[1]
            }}
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

    # @jwt_required()

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("price", type=float,
                            required=True, help="Price Fields Required")
        # data = request.get_json()
        data = parser.parse_args()
        if Item.find_by_name(name) is None:
           Item.insert_item(name, data['price'])
           return {"Message" : "Item Added Successfully"}
        else:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            query = f"UPDATE items SET price=? WHERE name=?"
            cursor.execute(query, (data['price'], name))
            connection.commit()
            connection.close()
            return {"name": name, "price" : data['price']}



        # myitem = next(filter(lambda x: x['name'] == name, items), None)
        # if myitem is None:
        #     item = {"name": name, "price": data['price']}
        #     items.insert(0, item)
        #     return items
        # else:
        #     myitem.update(data)
        #     return items


# class Student(Resource):
#     def get(self, name):
#         return {'student': name}


class Itemlist(Resource):
    # @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name" : row[1], "price" : row[2]})

        return {"items" : items}