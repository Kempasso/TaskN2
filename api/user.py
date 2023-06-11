from typing import Any, Dict

from flask import request, jsonify, Response
from flask_restx import Namespace, Resource

from services import user_service

user_namespace = Namespace('api/user')


@user_namespace.route('/')
class User(Resource):

    @staticmethod
    def post():
        username = request.json.get('username', None)
        if not username:
            return {"response": "Not enough data"}, 401
        elif not isinstance(username, str):
            return {"msg": "Username have to be in string format"}, 401
        exist_user_check = user_service.check_exist_username(username)
        if exist_user_check:
            return exist_user_check
        user = user_service.create_user(username)
        return {"user_id": user.id, "user_uuid": user.uuid}, 200
