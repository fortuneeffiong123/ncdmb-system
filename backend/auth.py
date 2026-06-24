from flask import Blueprint, request, jsonify

auth = Blueprint("auth", __name__)

# TEMPORARY hardcoded credentials — replace with database + hashed passwords
# before this goes anywhere near production or real users.
HARDCODED_USERNAME = "admin"
HARDCODED_PASSWORD = "ncdmb123"

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"message": "No data provided"}), 400

    username = data.get("username")
    password = data.get("password")

    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401