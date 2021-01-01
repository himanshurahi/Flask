from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "himanshu",
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
    return render_template("index.html")


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
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
        else:
            return jsonify({"error": "No Store Found"})
    # return name


@app.route("/store")
def get_store():
    return jsonify(stores)


@app.route("/store/<name>/item")
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
        else:
            return jsonify({"error": "No Item Found"})


@app.route("/store/<name>/item", methods=['POST'])
def store_item(name):
    try:
        requested_data = request.get_json()
        for store in stores:
            if(store['name'] == name):
                new_item = {
                    "name": requested_data['name'],
                    "price": requested_data['price']
                }
                store['items'].insert(0, new_item)
                return jsonify(store)
            else:
                return jsonify({"error": "No Item Found"})
    except:
        return jsonify("errro")


app.run(port=5000, debug=True)
