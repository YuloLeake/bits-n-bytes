import json

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    with open('my_app/artifacts/foo/test.json') as f:
        data = json.load(f)

    return jsonify(data)
