from flask import request
from .. import db
from . import shipment
from models.parcels import Shipment, Parcel
from schemas import shipment_schema


@shipment.post('/<parcel_id>')
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
        new_shipment.update_parcel_stock()  # updates parcel stock
        new_shipment.set_weight()  # set shipment total weight
        db.session.add(new_shipment)
        db.session.commit()

        resp['status'] = 'success'
        resp['msg'] = 'created new shipment'
        resp['data'] = shipment_schema.dump(new_shipment)

        status_code = 201
    else:
        # if parcel is not found close session
        # and send response back to client
        db.session.rollback()
        resp['status'] = 'error'
        resp['msg'] = f'product with id {parcel_id} not found'
        status_code = 404

    return resp, status_code


@shipment.patch('/<shipment_id>/<status_no>')
def update_shipment_status(shipment_id, status_no):
    """
    updates the shipment status and any additional
    detail thats sent via json (ideally this should
    be just a location update). The status describes
    three states (IN-TRANSIT), (PRE-DISPATCH), and (DELIVERED)
    each one is associated by a no from 1->n, (where n=3).

    This handler expects a shipment_id and the status number
    that the shipment is to be updated with, as url parameters
    but also allows for additional data to be sent via json, in the
    event that the current location needs to be updated as well.

    The handler exposes a PATCH endo
    """
    # find shipment object from db
    data = None
    try:
        data = request.get_json()
    except Exception:
        pass
    print(data)
    resp, status_code = {}, None
    shipment = Shipment.query.filter_by(shipment_id=shipment_id).first()
    if not shipment:
        resp['status'] = 'error'
        resp['msg'] = f'shipment with id {shipment_id} not found'
        resp['data'] = ''

        status_code = 404
    else:
        if data:
            for key, val in data.items():
                setattr(shipment, key, val)
        shipment.status = status_no
        db.session.commit()  # commit changes to db
        resp['status'] = 'success'
        resp['msg'] = 'shipment details updated'
        resp['data'] = ''

        status_code = 200
    return resp, status_code
