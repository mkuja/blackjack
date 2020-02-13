from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import User as UserModel
from db import db


class LogIn(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        user_actual_password = UserModel.find_by_username(args.get('username', None))
        user_actual_password = None if not user_actual_password else user_actual_password.password
        # If login success
        if user_actual_password and user_actual_password == args.get('password'):
            access_token = create_access_token(identity=args.get('username'))
            return {"access_token": access_token}, 200
        else:
            return {'message': f'Invalid username or password.'}, 403
