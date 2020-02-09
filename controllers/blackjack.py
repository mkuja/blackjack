# Game logic
from random import random
from math import floor
from models.hand import Hand


class Blackjack:
    deck = [
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
        "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS",
        "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
        "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
    ]

    @classmethod
    def draw_card(cls) -> str:
        """Draws a card.

        A card is a string in the format of value+kind.
        For example:
            2C for 2 of crosses.
            10D for 10 of diamonds.
            AH for ace of hearts.
            KS for kind of spades.

        Value is a number from 2 to 10, and one of J|Q|K|A for the honourables."""
        return cls.deck[floor(random() * len(cls.deck))]

    @staticmethod
    def evaluate_hand(hand: Hand):
        """Takes a Hand and returns the hand's current value."""
        cards = hand.card1, hand.card2, hand.card3, hand.card4, hand.card5
        cards = [card for card in cards if card]
        value = 0
        for card in cards:
            if card.startswith("10"):
                value += 10
            elif card.startswith("J") or card.startswith("Q") or card.startswith("K"):
                value += 10
            elif card.startswith("A"):  # Ace is 1 or 11
                value += 11
                if value > 21:
                    value -= 10
            else:  # Else use the digit in front of the str as value
                value += int(card[0])

        return value

    @staticmethod
    def is_splittable(hand: Hand):
        """Returns True if hand is a pair. False otherwise."""
        if hand.card3:
            return False
        elif hand.card1 == hand.card2 and hand.card2:
            return True
        else:
            raise Exception("Unknown error happened.")

    @staticmethod
    def decide_winner_hand(dealer_hand: Hand, player_hand: Hand) -> int:
        """Return negative int if dealer_hand wins. Return 0 if tie. Return positive int if player_hand wins."""
        dealer_hand = Blackjack.evaluate_hand(dealer_hand)
        player_hand = Blackjack.evaluate_hand(player_hand)

        if player_hand > 21:  # Player always loses when over 21
            return -1
        elif dealer_hand > 21:  # Then, if dealer goes over, she loses.
            return 1
        else:
            return player_hand - dealer_hand  # Bigger hand shall win.
