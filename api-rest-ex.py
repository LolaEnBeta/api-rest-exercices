from flask import Flask, jsonify, abort, request

app = Flask (__name__)

users = [
    {"userName": "User1",
    "id": 1,
    "email": "user1@hi.com",
    "state": False},

    {"userName": "User2",
    "id": 2,
    "email": "user2@hi.com",
    "state": False},

    {"userName": "User3",
    "id": 3,
    "email": "user3@hi.com",
    "state": False},
]


@app.route("/")
def index():
    return "Hello world!"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"List of users": users})

@app.route("/users/<int:id>", methods=["GET"])
def get_a_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify({"User": user})
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"User": "Not found"})

@app.route("/users", methods=["POST"])
def post_user():
    userName = request.json.get("userName")
    id = users[-1].get("id") + 1
    email = request.json.get("email")
    status = False
    users.append({"userName": userName, "id": id, "email": email, "status": status})
    return jsonify({"userName": userName, "id": id, "email": email, "status": status})

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify("User deleted")
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)
