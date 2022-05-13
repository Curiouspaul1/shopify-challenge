from core import db
from base import BaseModel
from datetime import datetime
from uuid import uuid4


class Address(BaseModel, db.Model):
    address_id = db.Column(db.String, default=str(uuid4()), primary_key=True)
    address_line_1 = db.Column(db.String(50), nullable=False)
    address_line_2 = db.Column(db.String(50))
    state_or_province = db.Column(db.String(50))
    postal_code = db.Column(db.String(6))
    last_update_time = db.Column(db.Date, default=datetime.utcnow())
    recipient_id = db.Column(db.String, db.ForeignKey('recipient.recipient_id'))
