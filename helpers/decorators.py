from flask import request

from services import user_service


def auth_required(func):
    def wrapper(*args, **kwargs):
        data = request.form
        if not isinstance(data.get('user_id', None), int) or not isinstance(data.get('user_uuid', None), str):
            return {'msg': 'Bad data format'}, 401
        check = user_service.check_user_auth(data.get('user_id'), data.get('user_uuid'))
        if 201 in check:
            result = func(*args, **kwargs)
            return result
        return check

    return wrapper
