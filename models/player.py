from db import db
from models import Hand
from errors import ArgumentError

class Player(db.Model):
    """Player models a player in game. Player has up to two hands of cards."""

    id = db.Column(db.Integer, primary_key=True)
    hand1 = db.ForeignKey("Hand.id")
    hand2 = db.ForeignKey("Hand.id")

    def __init__(self, hand1=db.null, hand2=db.null):
        if hand2 != db.null and hand1 == db.null:
            raise ArgumentError("Can't have hand2 set while hand1 is unset.")
        self.hand1 = hand1
        self.hand2 = hand2

    def add_hand(self, hand: Hand) -> None:
        """Add a Hand to the player."""
        if self.hand1 == db.null and self.hand2 == db.null:
            raise ArgumentError(
                "Trying to add a hand to player who already has 2 hands. A player can't have a third hand.")
        elif self.hand1 == db.null:
            self.hand1 = hand
        elif self.hand2 == db.null:
            self.hand2 = hand

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).next()