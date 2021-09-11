from functools import wraps

from exceptions.exception_authorization_error import AuthorizationError
from exceptions.exception_invalid_password import *
from exceptions.exception_non_existent_user import *
from exceptions.exception_user_email_not_unique import *
from exceptions.exception_validation_error import ValidationError
from exceptions.exception_resource_not_found import ResourceNotFoundException
from flask import jsonify, request
from helper import Helper
from service.service_security import ServiceSecurity
import traceback
from typing import List


class api():
    def authorization(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            data = request.headers.get('Authorization')

            try:
                service_security = ServiceSecurity()
                payload = service_security.validate_authorization(data)
                kwargs['email'] = payload.get('email')
                return f(*args, **kwargs)
            except AuthorizationError as error:
                return jsonify({"status": "authorization-error", "message": str(error)}), 403

        return decorated_function

    def rols_allowed(roles:List):
        def decorator(function):
            @wraps(function)
            def validate_schema(*args, **kwargs):
                try:
                    data = request.headers.get('Authorization')
                    service_security = ServiceSecurity()
                    payload = service_security.validate_authorization(data)

                    if payload.get('rol') in roles:
                        kwargs['rol'] = payload.get('rol')
                        return function(*args, **kwargs)

                    raise AuthorizationError('rol not allowed')
                except AuthorizationError as error:
                    return jsonify({"status": "validation-error", "message": str(error)}), 403
            return validate_schema
        return decorator

    def validator(schema):
        def decorator(function):
            @wraps(function)
            def validate_schema(*args, **kwargs):
                try:
                    Helper.validateJson(request.get_json(), schema)
                    return function(*args, **kwargs)
                except ValidationError as error:
                    return jsonify({"status": "validation-error", "message": str(error)}), 400
            return validate_schema
        return decorator

    def exception(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except ResourceNotFoundException as error:
                return jsonify({"status": "OK", "message": "Resource not found"}), 404
            except ValidationError as error:
                return jsonify({"status": "validation-error", "message": str(error)}), 400
            except InvalidPassword as error:
                return jsonify({"status": "invalid-userpass-error", "message": str(error)}), 401
            except Exception as error:
                tb = traceback.format_exc()
                return jsonify({"status": "server-error", "message": str(type(error)) + ' - ' + str(error) + ' - ' + tb }), 500
        return decorated_function
