from core import db


class BaseModel:
    id = db.Column(db.Integer, autoincrement=True)


class BaseModelPR:
    id = db.Column(db.Integer, primary_key=True)
