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


@shipment.patch('/<shipment_id>/status_no')
def update_shipment_status(shipment_id, status_no):
    # find shipment object from db
    resp, status_code = {}, None
    shipment = Shipment.query.filter_by(shipment_id=shipment_id).first()
    if not shipment:
        resp['status'] = 'error'
        resp['msg'] = f'shipment with id {shipment_id} not found'
        resp['data'] = ''

        status_code = 404
    else:
        shipment.status = status_no
        db.session.commit()  # commit changes to db
        resp['status'] = 'success'
        resp['msg'] = 'shipment status updated'
        resp['data'] = ''

        status_code = 200
    return resp, status_code
