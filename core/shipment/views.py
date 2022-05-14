from flask import request
from .. import db
from . import shipment
from models.parcels import Shipment, Parcel


@shipment.post('/shipment/<parcel_id>')
def new_shipment(parcel_id):
    """
    view function/handler thats responsible
    for creating a new shipment
    """
    data = request.get_json(force=True)
    resp, status_code = {}, None
    db.session.begin()  # create new session for db transaction
    # find product with given id
    parcel = Parcel.query.filter_by(parcel_id=parcel_id).first()
    if parcel:
        # create shipment add parcel to shipment
        new_shipment = Shipment(params=data)
        new_shipment.parcel = parcel
        db.session.add(new_shipment)
        db.session.commit()
    else:
        # if parcel is not found close session
        # and send response back to client
        db.session.rollback()
        resp['status'] = 'error'
        resp['msg'] = f'product with id {parcel_id} not found'
        status_code = 404

    return resp, status_code
