from flask import Flask
import os

INSTANCE_FOLDER = os.path.join(os.getcwd(), "instance")
TEMPLATES_FOLDER = os.path.join(os.getcwd(), r"guns\templates")


class DefaultConfig:
    ENV = "development"
    SECRET_KEY = "dev"


def create_app(config: str = None):
    app = Flask(__name__, instance_relative_config=True)

    # Default config #
    app.config.from_object(DefaultConfig)

    if config is not None:
        app.config.from_pyfile(config)

    # Registering Index's Blueprint #
    from .views import index

    app.register_blueprint(index.bp)

    return app
