import uuid

from flask import Response

from repositories import UserRepo, user_repository


class UserService:
    repository: UserRepo = user_repository

    def check_user_auth(self, user_id, user_uuid):
        user = self.repository.get_first_by_values(id=user_id, uuid=user_uuid)
        if not user:
            return "Don't authorized", 401
        else:
            return "Ok", 201

    def check_exist_username(self, username):
        user = self.repository.get_first_by_values(login=username)
        if user:
            return {"response": "User exist"}, 409
        return False

    def create_user(self, username):
        user_uuid = uuid.uuid4()
        user = self.repository.create(login=username, uuid=user_uuid)
        return user
