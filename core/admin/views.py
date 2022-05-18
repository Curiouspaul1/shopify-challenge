from . import admin
from .. import db
from flask import request, current_app
from models.parcels import Parcel, Category
from schemas import parcel_schema, parcels_schema, category_schema
from sqlalchemy.exc import IntegrityError
from typing import Optional


@admin.post('/parcel')
def create_product():
    """
    view function/handler thats responsible
    for creating a new parcel/product
    """
    data = request.get_json(force=True)
    resp, status_code = {}, None
    db.session.begin()  # new db transaction initiated
    # find the category and assign parcel to it
    category = Category.query.filter_by(id=data['category_id']).first()
    if not category:
        resp['status'] = 'error'
        resp['msg'] = f"category with id {data['categoty_id']} not found"
        resp['data'] = ''
        
        status_code = 404
        db.session.rollback()
    else:
        new_product = Parcel(params=data)
        new_product.category = category
        db.session.add(new_product)
        db.session.commit()  # commit changes to db

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
        for key, val in data.items():
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


@admin.get('/parcels/<page>')
def get_parcels(page: Optional[int] = 1):
    page = int(page)
    parcels = Parcel.query.order_by(Parcel.id).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False
    )
    print(parcels.items)
    resp, status_code = {
        'status': 'success',
        'msg': 'fetched parcels',
        'data': parcels_schema.dump(parcels.items)
    }, 200

    return resp, status_code


@admin.get('/parcel/<parcel_id>')
def get_parcel(parcel_id):
    resp, status_code = {}, None
    parcel = Parcel.query.filter_by(parcel_id=parcel_id).first()
    if parcel:
        resp['status'] = 'success'
        resp['msg'] = 'fetched parcel'
        resp['data'] = parcel_schema.dump(parcel)
        status_code = 200
    else:
        resp['status'] = 'error'
        resp['msg'] = f'parcel with id {parcel_id} not found'
        resp['data'] = ''

    return resp, status_code


@admin.post('/category')
def add_new_category():
    data = request.get_json()
    resp, status_code = {}, None
    new_category = Category(params=data)
    db.session.add(new_category)
    try:
        db.session.commit()
        resp['status'] = 'success'
        resp['msg'] = 'added new category'
        resp['data'] = category_schema.dump(new_category)

        status_code = 201
    except IntegrityError:
        resp['status'] = 'failed'
        resp['msg'] = f"category with name {data['name']} already exists"
        resp['data'] = ''

        status_code = 500

    return resp, status_code
