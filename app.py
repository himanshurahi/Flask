from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "new Store",
        "items": [
            {
                "name": "new item",
                "price": 2
            }
        ]
    }
]


@app.route("/")
def home():
    return "<h1>Himanshu Rahi</h1>"


@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": []
    }
    stores.insert(0, new_store)
    return jsonify(stores)


@app.route("/store/<name>")
def get_name(name):
    return name


@app.route("/store")
def get_store():
    return jsonify(stores)


app.run(port=5000, debug=True)
