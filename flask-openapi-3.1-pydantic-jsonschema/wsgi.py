import json
from pathlib import Path

from flask import Flask, redirect, jsonify

from swagger.routes import add_docs_blueprint


def create_app(schema_fp: Path) -> Flask:
    app = Flask(__name__)
    add_docs_blueprint(app, schema_fp)


    @app.route("/")
    def docs_redirect():
        return redirect('/doc')
    
    @app.route("/swagger.json")
    def swagger_file():
        with open(schema_fp) as f:
            return jsonify(json.load(f))

    return app

if __name__ == "__main__":
    create_app(Path('openapi.json').resolve()).run()
