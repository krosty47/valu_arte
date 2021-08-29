from app import app
from flask import jsonify


@app.route('/', methods=['GET'])
def get_articles():
    return jsonify({"Hello": "World"}), 200

