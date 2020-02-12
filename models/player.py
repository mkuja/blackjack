from db import db
from models.hand import Hand
from errors import ArgumentError


class Player(db.Model):
    """Player models a player in game. Player has up to two hands of cards."""

    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    hand_id1 = db.Column(db.Integer, db.ForeignKey("hand.id"))
    hand_id2 = db.Column(db.Integer, db.ForeignKey("hand.id"), nullable=True)
    hand1 = db.relationship('Hand', foreign_keys=[hand_id1])
    hand2 = db.relationship('Hand', foreign_keys=[hand_id2])

    def __init__(self, hand1: Hand, hand2=None):
        self.hand_id1 = hand1.id
        self.hand_id2 = hand2.id if hand2 else hand2

    def add_hand(self, hand: Hand) -> None:
        """Add a Hand to the player."""
        if self.hand1 and self.hand2:
            raise ArgumentError(
                "Trying to add a hand to player who already has 2 hands. A player can't have a third hand.")
        elif not self.hand1:
            self.hand1 = hand
        else:
            self.hand2 = hand

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).next()
