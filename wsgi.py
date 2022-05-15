# flake8: noqa

from core import create_app
import os

from models import (
    base, parcels,
    warehouses
)

app = create_app(os.getenv('APP_CONFIG') or 'default')

if __name__ == "__main__":
    app.run()
