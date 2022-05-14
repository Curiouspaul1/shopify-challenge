# flake8: noqa
from flask import Blueprint

admin = Blueprint("api", __name__)

from . import views
