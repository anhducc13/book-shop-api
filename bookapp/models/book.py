from bookapp.models import db, bcrypt
from datetime import datetime, timedelta
from flask_restplus import fields
from sqlalchemy.orm import relationship


class Book(db.Model):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode(), nullable=False, unique=True)
    author = db.Column(db.Unicode(), nullable=True)
    description = db.Column(db.Unicode(), nullable=True)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now)
    user_id_updated = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_active = db.Column(db.Boolean, default=True)
    image_link = db.Column(db.Text(), nullable=True)
    star = db.Column(db.SmallInteger, default=5)
    price = db.Column(db.Float, nullable=False)
    quantity_in_stock = db.Column(db.Integer, nullable=False)
    quantity_sold = db.Column(db.Integer, default=0)

    def update_attr(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

