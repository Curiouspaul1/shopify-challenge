# flake8: noqa
from flask import Blueprint

shipment = Blueprint("shipment", __name__)

from . import views
