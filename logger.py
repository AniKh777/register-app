import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(filename='/app/app.log', level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home route was accessed.")
    return "Logger is working!"

@app.route('/log', methods=['POST'])
def log_message():
    message = request.json.get('message')
    if message:
        app.logger.info(f"Received message: {message}")
        return jsonify({"message": "Log received"}), 200
    return jsonify({"error": "No message provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

