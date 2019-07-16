from flask_restplus import fields


class AuthSchema:
  schema_login_req = {
    'username': fields.String(required=True, description='user username'),
    'password': fields.String(required=True, description='user password')
  }
