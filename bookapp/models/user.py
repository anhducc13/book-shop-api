import enum
from bookapp.models import db, bcrypt
from datetime import datetime, timedelta
from flask_restplus import fields
from sqlalchemy.orm import relationship
from flask_user import UserMixin, user_manager


class Role(enum.Enum):
    """
    Role of a user in the system.
    """
    admin = 'admin'
    agent = 'agent'


class User(db.Model, UserMixin):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.TIMESTAMP, default=datetime.now)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    created_at = db.Column(db.TIMESTAMP, default=datetime.now)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.now)
    password_hash = db.Column(db.Text(), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    role = db.Column(db.Enum(Role), nullable=False, default=Role.agent)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def update_attr(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'role': self.role,
            'active': self.active
        }
