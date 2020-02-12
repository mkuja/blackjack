from db import db
from errors import HandFullError, ArgumentError


class Hand(db.Model):
    """Hand models a Player's hand, and has up to five cards."""

    __tablename__ = 'hand'
    id = db.Column(db.Integer, primary_key=True)
    card1 = db.Column(db.String(4), nullable=True)
    card2 = db.Column(db.String(4), nullable=True)
    card3 = db.Column(db.String(4), nullable=True)
    card4 = db.Column(db.String(4), nullable=True)
    card5 = db.Column(db.String(4), nullable=True)

    def __init__(self, *cards: str):
        """Argument cards is a list of cards to initialize a Hand with.

        A card is a string in the format of value+kind.
        For example:
            2C for 2 of crosses.
            10D for 10 of diamonds.
            AH for ace of hearts.
            KS for kind of spades.

            Value is a number from 2 to 10, and one of J|Q|K|A for the
            honourables."""
        if len(cards) > 5:
            raise ArgumentError("Too many arguments; A hand can hold a maximum of five cards.")
        cards = cards + tuple((5-len(cards)) * [None])
        self.card1, self.card2, self.card3, self.card4, self.card5 = cards

    def put_card(self, card: str) -> "Hand":
        """Put a card in hand."""
        if not self.card1:
            self.card1 = card
        elif not self.card2:
            self.card2 = card
        elif not self.card3:
            self.card3 = card
        elif not self.card4:
            self.card4 = card
        elif not self.card5:
            self.card5 = card
        else:
            raise HandFullError("This hand is already full. You can't add more cards to it.")
        return self

    def get_cards(self) -> list:
        return [eval(f"this.card{x}") for x in range(1, 6)]

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).next()
