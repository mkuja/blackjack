from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity  # Only identified players may play.

# Database stuff
from db import db
from models.game_table import GameTable
from models.player import Player
from models.hand import Hand
from models.user import User

from controllers.blackjack import Blackjack as BJ


class Play(Resource):

    @jwt_required
    def post(self):
        """JSON should be of format:

            {"action": "more"|"stay"|"insure"|"split"|"give_up"|"new_game"}


            With all actions the reply will be like:

            {"username": username,
            "player_hands": [
                {"first_card": somecard,
                "second_card": somecard2,
                "third_card": somecard3,
                "fourth_card": somecard4,
                "fifth_card": "none",
            ],
            "computer_hand": [
                { ... Same as hands, except the list will contain only one hand ... }
            ],
            "legit_actions": [ A list of legit game actions as listed above. ]
            }

        The hand (list containing cards) may have another hand for if user has split her hand.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('action', type=str, required=True)
        action = parser.parse_args().get('action', None)

        if action == 'new_game':
            player_hand = Hand(card1=BJ.draw_card(), card2=BJ.draw_card())
            computer_hand = Hand(card1=BJ.draw_card(), card2=BJ.draw_card())
            player_player = Player(hand1=player_hand)
            computer_player = Player(hand1=computer_hand)
            owner = User.find_by_username(get_jwt_identity())
            GameTable(player=player_player, computer=computer_player, owner=owner)
            db.session.add(owner)
            db.session.commit()
            return self.to_json(owner)
        elif action == 'give_up':
            pass
        elif action == 'split':
            # Allow only one split when 2nd hand is empty and when have exactly 2 cards of same value in hand.
            owner = User.find_by_username(get_jwt_identity())
            h1 = owner.table.player.hand1
            h2 = owner.table.player.hand2
            if not h2 and h1.card1 == h1.card2 and not h1.card3:
                h2.card1 = h1.card2
                h1.card2 = None
                db.session.add(owner)
                db.commit()
            else:
                return {'msg': "Split is allowed only on initial two cards of same value, and only once."}
        elif action == 'insure':
            pass
        elif action == 'stay':
            owner = User.find_by_username(get_jwt_identity())
            self.draw_for_computer(owner)
        elif action == 'more':
            #  Get the game for the current user
            user = User.find_by_username(get_jwt_identity())
            if not user.table:
                return {'msg': 'No open table for current user.'}
            user.table.player.hand1.put_card(BJ.draw_card())
            db.session.add(user)
            db.session.commit()
            return self.to_json(user)
        else:
            raise Exception("No valid action in json.")

    def to_json(self, owner):
        return {'username': owner.username,
                'player_hands': [
                    {
                        'first_card': owner.table.player.hand1.card1,
                        'second_card': owner.table.player.hand1.card2,
                        'third_card': owner.table.player.hand1.card3,
                        'fourth_card': owner.table.player.hand1.card4,
                        'fifth_card': owner.table.player.hand1.card5,
                        'legit_moves': BJ.get_legit_actions(owner.table.player.hand1),
                        'hand_value': BJ.evaluate_hand(owner.table.player.hand1),
                        'hand_over': owner.table.player.hand1.hand_over
                    },{
                        'first_card': owner.table.player.hand2.card1,
                        'second_card': owner.table.player.hand2.card2,
                        'third_card': owner.table.player.hand2.card3,
                        'fourth_card': owner.table.player.hand2.card4,
                        'fifth_card': owner.table.player.hand2.card5,
                        'legit_moves': BJ.get_legit_actions(owner.table.player.hand2),
                        'hand_value': BJ.evaluate_hand(owner.table.player.hand2),
                        'hand_over': owner.table.player.hand2.hand_over
                    }],
                'computer_hand': {
                        'first_card': owner.table.computer.hand1.card1,
                        'second_card': owner.table.computer.hand1.card2,
                        'third_card': owner.table.computer.hand1.card3,
                        'fourth_card': owner.table.computer.hand1.card4,
                        'fifth_card': owner.table.computer.hand1.card5,
                        'hand_value': BJ.evaluate_hand(owner.table.computer.hand1),
                        'hand_over': owner.table.computer.hand1.hand_over
                    }
                }