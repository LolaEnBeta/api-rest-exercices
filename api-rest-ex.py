from flask import Flask, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)
