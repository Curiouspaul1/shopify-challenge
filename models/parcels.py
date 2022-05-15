from core import db
from .base import BaseModel, BaseModelPR
from uuid import uuid4
from typing import Optional, Dict
from datetime import datetime as dt


class Status:
    DELIVERED = 1
    IN_TRANSIT = 2


class Parcel(BaseModel, db.Model):
    parcel_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    weight = db.Column(db.Float)
    quantity_in_stock = db.Column(db.Integer)
    date_created = db.Column(db.Date, default=dt.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    shipment_id = db.Column(db.String, db.ForeignKey('shipment.shipment_id'))

    def __init__(self, params: Optional[Dict] = None, **kwargs) -> None:
        super().__init__(**kwargs)
        if params:
            for key, val in params.items():
                setattr(self, key, val)
        elif len(kwargs.items()) > 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
        self.parcel_id = str(uuid4())

    def update_stock(self, quantity_shipped: int) -> None:
        # updates the stock according to amount
        # sent out for shipment
        self.quantity_in_stock -= quantity_shipped
        db.session.commit()


class Shipment(db.Model):
    shipment_id = db.Column(db.String, primary_key=True)
    status = db.Column(db.Integer)

    # sets a one-to-one mapping from shipment table to
    # parcel table; this will enable us assign a parcel
    # to a shipping
    parcel = db.relationship('Parcel', backref="shipment", uselist=False)

    parcel_quantity = db.Column(db.Integer, default=1)
    weight_ = db.Column(db.Float)
    destination = db.Column(db.String(100))
    current_location = db.Column(db.String(100))

    def __init__(self, params: Optional[Dict] = None, **kwargs) -> None:
        super().__init__(**kwargs)
        if params:
            for key, val in params.items():
                setattr(self, key, val)
        elif len(kwargs.items()) > 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
        self.shipment_id = str(uuid4())

    @property
    def weight(self):
        return self.weight_

    @weight.setter
    def set_weight(self):
        self.weight_ = self.parcel.weight * self.parcel_quantity


class Category(BaseModelPR, db.Model):
    name = db.Column(db.String(20))
    parcels = db.relationship('Parcel', backref='category')

    @staticmethod
    def add_categories():
        pass
