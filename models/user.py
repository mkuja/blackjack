from db import db


class User(db.Model):
    """User is someone who logs on to the api and username-field is that person's identity."""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # One-to-one relationship. The current unfinished game, if any.
    # game_id = db.relation(db.Integer, db.ForeignKey('game_table.id'), uselist=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.game = db.null

    @classmethod
    def find_by_username(cls, username: str) -> "User":
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, id: int) -> "User":
        return cls.query.filter_by(id=id).first()

