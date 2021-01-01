from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.secret_key = 'rahi'
api = Api(app)

jwt = JWT(app, authenticate, identity)


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
        item = next(filter(lambda x: x['name'] == name, items), 'Not Found')
        print(item)
        return {'item': item}, 200 if item else 404
        # for item in items:
        #     if(item['name'] == name):
        #         return item
        #     else:
        #         return {"error": "No Item Found"}, 404

    def post(self, name):
        requested_data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is not None:
            return {"Error_msg": f"Item {name} already Exist"}

        item = {"name": name, "price": requested_data['price']}
        items.append(item)
        return items

    def delete(self, name):
        # requested_data = request.get_json()
        myitems = next(filter(lambda x: x['name'] != name, items), None)
        return myitems

    # @jwt_required()
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("price", type=float,
                            required=True, help="Price Fields Required")
        # data = request.get_json()
        data = parser.parse_args()
        myitem = next(filter(lambda x: x['name'] == name, items), None)
        if myitem is None:
            item = {"name": name, "price": data['price']}
            items.insert(0, item)
            return items
        else:
            myitem.update(data)
            return items


# class Student(Resource):
#     def get(self, name):
#         return {'student': name}


class Itemlist(Resource):
    # @jwt_required()
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<name>")
api.add_resource(Itemlist, "/items")
# api.add_resource(Student, "/student/<name>")


app.run(port=5001, debug=True)
