from flask import Flask
from .extensions import (
    db, migrate, ma
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
    ma.init_app(app)

    # register flask blueprints
    from .admin import admin
    from .shipment import shipment

    app.register_blueprint(shipment, url_prefix='/shipment')
    app.register_blueprint(admin, url_prefix='/admin')

    return app
