from core import db


class BaseModelPR:
    id = db.Column(db.Integer, primary_key=True)
