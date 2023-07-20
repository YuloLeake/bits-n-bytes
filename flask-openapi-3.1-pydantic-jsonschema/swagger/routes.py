import json

from flask import Blueprint, Flask, render_template, url_for


def add_docs_blueprint(app: Flask) -> None:

    docs_blueprint = Blueprint(
        'swagger',
        import_name=__name__,
        static_folder='static',
        template_folder='templates',
        url_prefix='/doc'
    )

    @docs_blueprint.route("/")
    def render_swagger():

        config = {
            "app_name": "Swagger UI",
            "dom_id": "#swagger-ui",
            "url": url_for("swagger_file"),
            "layout": "StandaloneLayout",
            "deepLinking": True,
        }
        fields = {
            # Some fields are used directly in template
            # "base_url": base_url,
            "app_name": config.pop("app_name"),
            # Rest are just serialized into json string for inclusion in the .js file
            "config_json": json.dumps(config),
        }

        return render_template("index.html", **fields)


    app.register_blueprint(docs_blueprint)
