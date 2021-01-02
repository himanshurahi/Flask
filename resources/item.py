from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity
import sqlite3
from models.User import User
from flask_bcrypt import Bcrypt
from models.Item import ItemModel

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
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"Msg": "Empty"}

    def post(self, name):
        requested_data = request.get_json()
        if ItemModel.find_by_name(name) is not None:
            return {"Message": "Item Already Exist"}
        else:
            return ItemModel.insert_item(name, requested_data['price'])

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = f"DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name, ))
        connection.commit()
        connection.close()

        return {"message": "Item Deleted Successfully."}

    # @jwt_required()

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("price", type=float,
                            required=True, help="Price Fields Required")
        # data = request.get_json()
        data = parser.parse_args()
        if ItemModel.find_by_name(name) is None:
            ItemModel.insert_item(name, data['price'])
            return {"Message": "Item Added Successfully"}
        else:
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            query = f"UPDATE items SET price=? WHERE name=?"
            cursor.execute(query, (data['price'], name))
            connection.commit()
            connection.close()
            return {"name": name, "price": data['price']}


class Itemlist(Resource):
    # @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name": row[1], "price": row[2]})

        return {"items": items}
