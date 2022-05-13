from core import db
from base import BaseModel
from uuid import uuid4


class Warehouse(BaseModel, db.Model):
    warehouse_id = db.Column(db.String, default=str(uuid4()))
    name = db.Column(db.String(100))
    