from db import db


class Game(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    player1 = db.Column(db.ForeignKey("Player.id"), nullable=False)
    player2 = db.Column(db.ForeignKey("Player.id"), nullable=False)
    playername = db.Column(db.ForeignKey('User.id'))

    def __init__(self, player1, player2, playername):
        self.player1 = player1
        self.player2 = player2

    @classmethod
    def find_by_id(cls, id):
        return db.query.get(id)