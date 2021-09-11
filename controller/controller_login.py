from app import app
from flask import jsonify, request
from service.service_login import ServiceLogin
from decorators.api_base import api
from models.model_user import UserModel


@app.route('/api/v1/login', methods=['POST'])
@api.validator(UserModel.jsonSchema())
@api.exception
def post_login():
    serviceLogin = ServiceLogin()
    parameters = request.get_json()
    token = serviceLogin.validate_user(
        parameters.get("email"), parameters.get("password"))
    return jsonify({"status": "OK", "token": token}), 200