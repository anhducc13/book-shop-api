from flask_restplus import fields


class AdminSchema:
  schema_user_req = {
    'username': fields.String(required=True, description='username'),
    'email': fields.String(required=True, description='email'),
    'role': fields.String(required=False, description='Role user')
  }

  schema_user_res = {
    'id': fields.Integer(required=True, description='user id'),
    'username': fields.String(required=True, description='username'),
    'email': fields.String(required=True, description='email'),
    'phone_number': fields.String(required=True, description='phone number'),
    'created_at': fields.DateTime(required=True, description='created at user'),
    'updated_at': fields.String(required=True, description='updated at user'),
    'role': fields.String(required=True, description='role of user'),
    'active': fields.Boolean(required=True, description='user is active or none')
  }
