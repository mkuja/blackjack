import os
import sys

sys.path.append(os.getcwd())

import unittest
from models.user import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask



class TestUserModel(unittest.TestCase):

    def setUp(self) -> None:
        app = Flask(__name__, static_folder="build/static", template_folder="build")
        app.secret_key = 'unittest'
        db = SQLAlchemy()
        db.init_app(app)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unittests.db'
        self.app = app
        self.db = db
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self) -> None:
        pass

    def test_user_create(self):
        user = User('herne543567', 'salasana')
        self.db.session.add(user)
        fuser = user.find_by_username("herne543567")
        self.assertEqual(fuser.id, user.id)


if __name__ == '__main__':
    unittest.main()
