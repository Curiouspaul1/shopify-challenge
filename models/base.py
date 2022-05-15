from core import db


class BaseModel:
    seq = db.Sequence(
        'id', increment=1,
        metadata=db.Model.metadata
    )
    id = db.Column(
        db.Integer, seq,
        server_default=seq.next_value()
    )


class BaseModelPR:
    id = db.Column(db.Integer, primary_key=True)
