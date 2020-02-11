from db import db
from .player import Player
from .user import User


class GameTable(db.Model):
    """GameTable models blackjack table, and has Players. GameTable also has owner. Owner provides it's identity, so
    correct GameTable can be loaded."""

    id = db.Column(db.Integer(), primary_key=True)
    player = db.Column(db.ForeignKey("Player.id"), nullable=False)
    computer = db.Column(db.ForeignKey("Player.id"), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('User.id'))

    def __init__(self, player: Player, computer: Player, owner: User):
        self.player = player
        self.computer = computer
        self.owner = owner

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

