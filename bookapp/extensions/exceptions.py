from werkzeug.exceptions import HTTPException as BaseHTTPException
from bookapp.extensions.response_wrapper import wrap_response
from bookapp import models


class HTTPException(BaseHTTPException):
    def __init__(self, code=400, message=None, errors=None):
        super().__init__(description=message, response=None)
        self.code = code
        self.errors = errors

    def __str__(self):
        code = self.code if self.code is not None else "???"
        return self.description


class BadRequestException(HTTPException):
    def __init__(self, message='Bad Request', errors=None):
        super().__init__(code=400, message=message, errors=errors)


class NotFoundException(HTTPException):
    def __init__(self, message='Resource Not Found', errors=None):
        super().__init__(code=404, message=message, errors=errors)


class UnAuthorizedException(HTTPException):
    def __init__(self, message='UnAuthorized', errors=None):
        super().__init__(code=401, message=message, errors=errors)


class ForbiddenException(HTTPException):
    def __init__(self, message='Permission Denied', errors=None):
        super().__init__(code=403, message=message, errors=errors)


class ConflictException(HTTPException):
    def __init__(self, message='Conflict', errors=None):
        super().__init__(code=409, message=message, errors=errors)


def global_error_handler(e):
    models.db.session.rollback()
    code = 500
    errors = None
    if isinstance(e, BaseHTTPException):
        code = e.code
    if isinstance(e, HTTPException):
        errors = e.errors
    res = wrap_response(None, str(e), code)
    if errors:
        res[0]['errors'] = errors
    return res