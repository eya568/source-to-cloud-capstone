import os
import socket
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "devopsdb")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")


def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=3,
    )


@app.route("/")
def index():
    return jsonify({
        "message": "Source To Cloud - Capstone API",
        "served_by": socket.gethostname(),
    })


@app.route("/health")
@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return jsonify({
            "status": "healthy",
            "db": "connected",
            "host": socket.gethostname(),
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "db": "unreachable",
            "error": str(e),
        }), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
