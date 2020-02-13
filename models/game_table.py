from db import db
from .player import Player
from .user import User
from datetime import datetime


class GameTable(db.Model):
    """GameTable models blackjack table, and has Players. GameTable also has owner. Owner provides it's identity, so
    correct GameTable can be loaded."""

    __tablename__ = "game_table"
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    computer_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player = db.relationship('Player', foreign_keys=[player_id])
    computer = db.relationship('Player', foreign_keys=[computer_id])

    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User')

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

