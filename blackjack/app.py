from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT, jwt_required, timedelta
from blackjack.security import authenticate, identity
from blackjack.db import db

import os.path

from blackjack.resources.user import User

# Config
app = Flask(__name__, static_folder="build/static", template_folder="build")
app.secret_key = 'test'

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)

if not os.path.isfile("test.db"):
    db.create_all(app=app)

jwt = JWT(app, authenticate, identity)

# Resource endpoints.
api = Api(app)
api.add_resource(User, '/user')


@app.route("/")
def react_app():
    from blackjack.db import db
    return render_template('index.html')

app.debug=True
app.run(host='0.0.0.0')