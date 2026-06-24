from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# =========================
# DATABASE CONFIG
# =========================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "ncdmb_db"   # ⚠️ IMPORTANT: make sure this matches your DB
}

# =========================
# DB CONNECTION
# =========================
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# =========================
# HOME
# =========================
@app.route("/")
def home():
    return jsonify({"message": "NCDMB System API Running"})

# =========================
# GET ALL EQUIPMENT
# =========================
@app.route('/equipment', methods=['GET'])
def get_equipment():
    db = None
    cursor = None

    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM equipment")
        data = cursor.fetchall()

        return jsonify({
            "status": "success",
            "data": data
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# =========================
# ADD EQUIPMENT
# =========================
@app.route('/equipment', methods=['POST'])
def add_equipment():
    db = None
    cursor = None

    try:
        data = request.json

        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        INSERT INTO equipment (name, type, location, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            data.get('name'),
            data.get('type'),
            data.get('location'),
            data.get('status')
        )

        cursor.execute(sql, values)
        db.commit()

        return jsonify({
            "status": "success",
            "message": "Equipment added successfully"
        }), 201

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# =========================
# UPDATE EQUIPMENT
# =========================
@app.route('/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    db = None
    cursor = None

    try:
        data = request.json

        db = get_db_connection()
        cursor = db.cursor()

        sql = """
        UPDATE equipment 
        SET name=%s, type=%s, location=%s, status=%s
        WHERE id=%s
        """

        values = (
            data.get('name'),
            data.get('type'),
            data.get('location'),
            data.get('status'),
            id
        )

        cursor.execute(sql, values)
        db.commit()

        return jsonify({
            "status": "success",
            "message": "Equipment updated successfully"
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# =========================
# DELETE EQUIPMENT
# =========================
@app.route('/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    db = None
    cursor = None

    try:
        db = get_db_connection()
        cursor = db.cursor()

        cursor.execute("DELETE FROM equipment WHERE id=%s", (id,))
        db.commit()

        return jsonify({
            "status": "success",
            "message": "Equipment deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(debug=True)