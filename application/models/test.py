# from .base_model import BaseModel
from application.extensions import db
from datetime import date


class test_table(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True, comment="id")
    name_str = db.Column(db.String(50), nullable=False, comment="名称")
    name_var = db.Column(db.VARCHAR(50), default="栗子")
    name_nvar = db.Column(db.NVARCHAR(50))
    is_deleted = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date, default=date)
    flob = db.Column(db.Float(10, 2))
    Flo = db.Column(db.FLOAT(10, 2))
    dec = db.Column(db.DECIMAL(10, 3))



    def __repr__(self):
        return "test table"
