from typing import Any, Dict

from flask import request
from flask_restx import Namespace, Resource

from repositories import user_repository
from services import user_service

user_namespace = Namespace('api/user')


@staticmethod
@user_namespace.route('/')
class User(Resource):

    @staticmethod
    def post():
        username = request.json.get('username')
        user = user_service.create_user(username)
        return {"user_id": user.id, "user_uuid": user.uuid}
