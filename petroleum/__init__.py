from flask import Flask
from petroleum.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from petroleum.errors.handlers import errors
    from petroleum.main.routes import main
    app.register_blueprint(errors)
    app.register_blueprint(main)

    return app
