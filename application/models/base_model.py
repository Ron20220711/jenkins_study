from application.extensions import db
from datetime import datetime


class BaseModel(db.Model):
    '''
    db base model
    '''
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="修改时间")
