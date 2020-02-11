from db import db
from .player import Player
from .user import User


class GameTable(db.Model):
    """GameTable models blackjack table, and has Players. GameTable also has owner. Owner provides it's identity, so
    correct GameTable can be loaded."""

    __tablename__ = "game_table"
    id = db.Column(db.Integer(), primary_key=True)
    player = db.Column(db.ForeignKey("player.id"), nullable=False)
    computer = db.Column(db.ForeignKey("player.id"), nullable=False)
    #owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, player: Player, computer: Player):
        self.player = player
        self.computer = computer
        #self.owner = owner

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)

