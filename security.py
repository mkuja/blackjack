from .models.user import User
from werkzeug.security import safe_str_cmp


def authenticate(user: str, password: str):
    raise Exception("authenticate")
    _user = User.find_by_username(user)
    if _user.username and _user.password == password:
        return _user

def identity(payload):
    raise Exception("identity")
    user_id = payload['identity']
    return User.find_by_id(user_id)