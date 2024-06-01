from flask import Flask, request, jsonify
import sqlite3
import os


app = Flask(__name__)


def get_db_connection():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, '../pc_specs.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None


@app.route("/")
def home():
    return 'This is the API root'


@app.route("/computers", methods=['GET'])
def get_computers():
    processor = request.args.get('processor')
    gpu = request.args.get('gpu')
    motherboard = request.args.get('motherboard')
    ram = request.args.get('ram')

    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection error"}), 500

    query = "SELECT * FROM specs_tb WHERE 1=1"
    params = []

    if processor:
        query += " AND processor LIKE ?"
        params.append(f"%{processor}%")
    if gpu:
        query += " AND gpu LIKE ?"
        params.append(f"%{gpu}%")
    if motherboard:
        query += " AND motherboard LIKE ?"
        params.append(f"%{motherboard}%")
    if ram:
        query += " AND ram LIKE ?"
        params.append(f"%{ram}%")

    try:
        cursor = conn.execute(query, params)
        products = cursor.fetchall()
        conn.close()
        products_list = [dict(product) for product in products]
        return jsonify(products_list)
    except sqlite3.Error as e:
        print(f"Query execution error: {e}")
        return jsonify({"error": "Query execution error"}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "Unexpected server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
