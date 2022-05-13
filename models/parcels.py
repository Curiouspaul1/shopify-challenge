from core import db
from base import BaseModel, BaseModelPR
from uuid import uuid4


class Status:
    DELIVERED = 1
    IN_TRANSIT = 2


class Parcel(BaseModel, db.Model):
    parcel_id = db.Column(db.String, default=str(uuid4()), primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    status = db.Column(db.Integer)
    tracking_id = db.Column(db.String, default=str(uuid4()))
    destination = db.Column(db.String(100))
    current_location = db.Column(db.String(100))
    weight = db.Column(db.Float)
    date_sent_out = db.Column(db.Date)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    sender = db.relationship('Sender', backref='parcel', uselist=False)
    recipient = db.relationship('Recipient', backref='parcel', uselist=False)


class Sender(BaseModel, db.Model):
    sender_id = db.Column(db.String, default=str(uuid4()), primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(60))
    telephone = db.Column(db.String(20))


class Recipient(BaseModel, db.Model):
    recipient_id = db.Column(db.String, default=str(uuid4()))
    address = db.relationship('Address', backref='recipient_address')
    name = db.Column(db.String(50))
    email = db.Column(db.String(60))
    telephone = db.Column(db.String(20))


class Category(BaseModelPR, db.Model):
    name = db.Column(db.String(20))
    parcels = db.relationship('Parcel', backref='category')