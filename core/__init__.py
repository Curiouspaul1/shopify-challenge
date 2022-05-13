from flask import Flask
from extensions import (
    db, migrate
)
from config import config_options


def create_app(config_name: str) -> Flask:
    """
    initializes and configures flask app instance

    param(s):: config_name <str>: name of the config option
    to be used to configure the application
    """

    app = Flask(__name__)

    # configure flask app
    app.config.from_object(config_options[config_name])

    # configure extensions with app instance
    db.init_app(app)
    migrate.init_app(app, db)

    # register flask blueprints

    return app
