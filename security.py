from models.user import User
from werkzeug.security import safe_str_cmp


def authenticate(user: str, password: str) -> User:
    _user = User.find_by_username(user)
    if _user and safe_str_cmp(User.find_by_username(user).password, password):
        return _user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id).first()
