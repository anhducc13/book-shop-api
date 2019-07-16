from flask_restplus import Namespace, Resource
from flask import request

from bookapp import schemas, models

ns = Namespace('admin', description='Admin operators')

_user_req = ns.model(
  'user_request', schemas.AdminSchema.schema_user_req)

_user_res = ns.model(
  'user_response', schemas.AdminSchema.schema_user_res)


@ns.route('/users')
class UserList(Resource):
  @ns.marshal_list_with(_user_res)
  def get(self):
    users = models.User.query.all()
    return users


@ns.route('/user')
class UserAdd(Resource):
  @ns.expect(_user_req, validate=True)
  @ns.marshal_with(_user_res)
  def post(self):
    pass


@ns.route('/user/<int:user_id>')
class User(Resource):
  @ns.marshal_with(_user_res)
  def get(self, user_id):
    pass

  @ns.doc('delete user with id')
  def delete(self, user_id):
    pass

  @ns.doc('update user with id')
  def put(self, user_id):
    pass
