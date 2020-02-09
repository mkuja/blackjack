from flask_restful import Resource, reqparse
from models.user import User as UserModel
from db import db


class SignIn(Resource):

    def post(self):
        """"Create a new user, if doesn't exist."""
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        if UserModel.find_by_username(args.get('username', None)):
            return {'message': 'That user already exists.'}, 500
        else:
            new_user = UserModel(args['username'], args['password'])
            db.session.add(new_user)
            db.session.commit() # Write to db.
            return {'message': f'User {args["username"]} was created.'}, 201

