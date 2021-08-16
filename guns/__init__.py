import os

from flask import Flask

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

    # Send e-mail
    from .utils.email import read_template, get_email_credentials, send_email
    template = read_template(os.path.join(app.instance_path, "call_us_email.txt"))
    email, password = get_email_credentials(os.path.join(app.instance_path, "email-connection.ini"))
    send_email(email, password, template, "Luan")

    return app
