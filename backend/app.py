from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

from auth import auth
app.register_blueprint(auth)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "ncdmbserver123",
    "database": "ncdmb_db"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

REQUIRED_FIELDS = ["name", "type", "location", "status", "recommendation"]

def validate_equipment_data(data):
    if not data:
        return "No data provided"
    missing = [f for f in REQUIRED_FIELDS if f not in data or data[f] in (None, "")]
    if missing:
        return f"Missing required field(s): {', '.join(missing)}"
    return None

@app.route("/")
def home():
    return jsonify({"message": "NCDMB API Running"})

@app.route("/equipment", methods=["GET"])
def get_equipment():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipment")
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/equipment", methods=["POST"])
def add_equipment():
    data = request.get_json(silent=True)
    error = validate_equipment_data(data)
    if error:
        return jsonify({"error": error}), 400
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO equipment (name, type, location, status, recommendation)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data["name"], data["type"], data["location"], data["status"], data["recommendation"]
        ))
        conn.commit()
        return jsonify({"message": "Added successfully", "id": cursor.lastrowid}), 201
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/equipment/<int:id>", methods=["PUT"])
def update_equipment(id):
    data = request.get_json(silent=True)
    error = validate_equipment_data(data)
    if error:
        return jsonify({"error": error}), 400
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE equipment
            SET name=%s, type=%s, location=%s, status=%s, recommendation=%s
            WHERE id=%s
        """, (
            data["name"], data["type"], data["location"], data["status"], data["recommendation"], id
        ))
        if cursor.rowcount == 0:
            return jsonify({"error": f"No equipment found with id {id}"}), 404
        conn.commit()
        return jsonify({"message": "Updated successfully"})
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/equipment/<int:id>", methods=["DELETE"])
def delete_equipment(id):
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipment WHERE id=%s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": f"No equipment found with id {id}"}), 404
        return jsonify({"message": "Deleted successfully"})
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(debug=False)