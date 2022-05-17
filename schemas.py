# this file contains schema for representation of
# database model objects in json. This means i can
# use these schemas to transform any orm object to
# serializable format that i can then return as json
# this is made possible by the flask-marshmallow extension

# flake8: noqa

from core import ma
from models.parcels import Parcel, Shipment, Category


class ParcelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Parcel

parcel_schema = ParcelSchema() # for a single object
parcels_schema = ParcelSchema(many=True)


class ShipmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shipment

shipment_schema = ParcelSchema() # for a single object
shipments_schema = ParcelSchema(many=True)


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

category_schema = CategorySchema() # for a single object
categories_schema = CategorySchema(many=True)
