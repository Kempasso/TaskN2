from flask import Flask

from api.user import user_namespace
from api.files import files_namespace
from repositories import create_tables

from flask_restx import Api

from settings import Config


def create_app(config: Config) -> Flask:
    app: Flask = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def configure_app(app):
    api = Api(app)
    api.add_namespace(files_namespace)
    api.add_namespace(user_namespace)


if __name__ == '__main__':
    configs = Config()
    application = create_app(configs)
    configure_app(application)
    create_tables()
    application.run(debug=True, host="0.0.0.0", port=8000)
