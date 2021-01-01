from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [{
    "name": "himanshurahi",
    "price": 1
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

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}


class Itemlist(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, "/item/<name>")
api.add_resource(Itemlist, "/items")
# api.add_resource(Student, "/student/<name>")


app.run(port=5001, debug=True)
