from flask import Flask, request, jsonify
import sqlite3
import os


app = Flask(__name__)


def init_db():
    db_path = 'db_data/users.db'
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def home():
    return "Welcome to the Register App!"


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
   
    conn = sqlite3.connect('db_data/users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()
   
    return jsonify({"message": "User registered successfully!"})


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
