from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"


# Dummy DB function (will be mocked in tests)
def get_db_connection():
    raise Exception("DB not available")


@app.route('/')
def dashboard():
    try:
        conn = get_db_connection()
        return render_template('dashboard.html')
    except Exception:
        return "dashboard fallback rendered", 200


@app.route('/api/actors')
def get_actors():
    try:
        conn = get_db_connection()
        return jsonify({"actors": []})
    except Exception:
        return jsonify({"error": "Database connection failed"}), 500


@app.route('/api/films')
def get_films():
    try:
        conn = get_db_connection()
        return jsonify({"films": []})
    except Exception:
        return jsonify({"error": "Database connection failed"}), 500


if __name__ == '__main__':
    app.run(debug=True)