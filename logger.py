import logging
from flask import Flask


app = Flask(__name__)


logging.basicConfig(filename='/app/app.log', level=logging.INFO)


@app.route('/')
def home():
    app.logger.info("Home route was accessed.")
    return "Logger is working!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
