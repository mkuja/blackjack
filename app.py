from flask import Flask, render_template, jsonify, request
from flask_restful import Api
from .security import authenticate, identity
from .db import db
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

import os.path

# Resources
from .resources.create_user import CreateUser
from .resources.log_in import LogIn
from .resources.play import Play

# Config
app = Flask(__name__, static_folder="build/static", template_folder="build")
app.secret_key = 'test'

#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)

if not os.path.isfile("test.db"):
    db.create_all(app=app)

api = Api(app)
jwt = JWTManager(app)

# Routing endpoints
api.add_resource(CreateUser, '/create_user')
api.add_resource(LogIn, '/log_in')
api.add_resource(Play, '/play')

@app.route("/")
def react_app():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0')