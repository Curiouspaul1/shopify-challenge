# this file contains schema for representation of
# database model objects in json. This means i can
# use these schemas to transform any orm object to
# serializable format that i can then return as json
# this is made possible by the flask-marshmallow extension

# flake8: noqa

from core import ma
from models.parcels import Parcel


class ParcelSchema(ma.Schema):
    class Meta:
        model = Parcel

parcel_schema = ParcelSchema() # for a single object
parcels_schema = ParcelSchema(many=True)
