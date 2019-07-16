from flask_restplus import Namespace, Resource
from flask import request

from bookapp import schemas, models

ns = Namespace('auth', description='Auth operators')

_login_req = ns.model(
  'login_request', schemas.AuthSchema.schema_login_req)


@ns.route('/login')
class Login(Resource):
  @ns.expect(_login_req, validate=True)
  def post(self):
    data = request.json or request.args
    user = models.User.query.filter().first()
    print(user.roles)
    return data, 200
