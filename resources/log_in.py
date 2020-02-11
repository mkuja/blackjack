from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from ..models.user import User as UserModel
from ..db import db


# @app.route('/login', methods=['POST'])
# def login():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400
#
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
#     if not username:
#         return jsonify({"msg": "Missing username parameter"}), 400
#     if not password:
#         return jsonify({"msg": "Missing password parameter"}), 400
#
#     if username != 'test' or password != 'test':
#         return jsonify({"msg": "Bad username or password"}), 401
#
#     # Identity can be any data that is json serializable
#     access_token = create_access_token(identity=username)
#     return jsonify(access_token=access_token), 200

class LogIn(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()
        user_actual_password = UserModel.find_by_username(args.get('username', None)).password
        # If login success
        if user_actual_password and user_actual_password == args.get('password'):
            access_token = create_access_token(identity=args.get('username'))
            return {"access_token": access_token}, 200
        else:
            return {'message': f'Invalid username or password.'}, 403
