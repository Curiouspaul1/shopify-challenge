from . import admin
from .. import db
from flask import request, current_app
from models.parcels import Parcel
from schemas import parcel_schema, parcels_schema
from typing import Optional


@admin.post('/parcel')
def create_product():
    """
    view function/handler thats responsible
    for creating a new parcel/product
    """
    data = request.get_json(force=True)
    resp, status_code = {}, None
    new_product = Parcel(params=data)
    db.session.add(new_product)
    db.session.commit()

    resp['status'] = 'success'
    resp['msg'] = 'added new inventory successfully'
    resp['data'] = parcel_schema.dump(new_product)
    status_code = 201

    return resp, status_code


@admin.route('/parcel/<parcel_id>', methods=['PATCH', 'PUT'])
def edit_parcel(parcel_id):
    """
    This is useful for making changes of any size
    to the resource, perhaps one or more fields
    of the resource need to be edited.
    It exposes a PATCH/PUT request endpoint
    """
    data = request.get_json(force=True)
    resp, status_code = {}, None

    # find the parcel and apply change
    parcel = Parcel.query.filter_by(parcel_id=parcel_id).first()
    if not parcel:
        resp['status'] = 'error'
        resp['msg'] = f'parcel with id {parcel_id} not found'
        resp['data'] = ''
        status_code = 404
    else:
        for key, val in data:
            setattr(parcel, key, val)
        db.session.commit()
        resp['status'] = 'success'
        resp['msg'] = 'updated parcel successfully'
        resp['data'] = ''

        status_code = 201
    return resp, status_code


@admin.delete('/parcel/<parcel_id>')
def delete_parcel(parcel_id):
    """
    Used to delete a resource from the db
    """
    # find parcel and delete
    parcel = Parcel.query.filter_by(parcel_id=parcel_id).first()
    db.session.delete(parcel)
    db.session.commit()

    resp, status_code = {
        'status': 'success',
        'msg': f'deleted parcel with id {parcel_id}',
        'data': ''
    }, 200
    return resp, status_code


@admin.get('/parcel/<page>')
def get_parcels(page: Optional[int] = 1):
    page = int(page)
    parcels = Parcel.query.order_by(Parcel.id).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    resp, status_code = {
        'status': 'success',
        'msg': 'fetched parcels',
        'data': parcels_schema.dump(parcels)
    }, 200

    return resp, status_code
