from bookapp.models import db, bcrypt
from datetime import datetime, timedelta
from flask_restplus import fields
from sqlalchemy.orm import relationship


class Category(db.Model):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text(), nullable=False, unique=True)
    description = db.Column(db.Unicode(), nullable=True)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now)
    user_id_updated = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_active = db.Column(db.Boolean, default=True)

    def update_attr(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


category_book_table = db.Table(
    'category_book',
    db.Model.metadata,
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)
