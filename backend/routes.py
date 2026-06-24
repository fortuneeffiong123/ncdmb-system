from app import app, mysql
from flask import request, jsonify

@app.route("/equipment", methods=["POST"])
def add_equipment():
    data = request.json

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO equipment (name, type, location, status, image_url)
        VALUES (%s, %s, %s, %s, %s)
    """, (data["name"], data["type"], data["location"], data["status"], data["image_url"]))

    mysql.connection.commit()
    return jsonify({"message": "Equipment added"})


@app.route("/equipment", methods=["GET"])
def get_equipment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM equipment")
    data = cur.fetchall()

    return jsonify(data)


@app.route("/equipment/<int:id>", methods=["PUT"])
def update_equipment(id):
    data = request.json

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE equipment
        SET name=%s, type=%s, location=%s, status=%s
        WHERE id=%s
    """, (data["name"], data["type"], data["location"], data["status"], id))

    mysql.connection.commit()
    return jsonify({"message": "Updated"})


@app.route("/equipment/<int:id>", methods=["DELETE"])
def delete_equipment(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM equipment WHERE id=%s", (id,))
    mysql.connection.commit()

    return jsonify({"message": "Deleted"})