#!/usr/bin/python3


from flask import Flask, jsonify, abort, request, make_response
app = Flask(__name__)

users = {
        "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return("Welcome to the Flask API!")


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/status")

def status():
    return("ok")

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.json:
        abort(400, description="Request body must be JSON")

    new_user = request.json
    username = new_user.get("username")

    if username in users:
        abort(400, description="User already exists")

    users[username]= {
        "username": username,
        "name": new_user.get("name"),
        "age": new_user.get("age"),
        "city": new_user.get("city")
    }

    return jsonify({"message": "User added successfully", "user": users[username]}), 201

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": str(error.description)}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": str(error.description)}), 404)

if __name__ == "__main__":
    app.run(debug=True)
