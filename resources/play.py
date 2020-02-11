from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity  # Only identified players may play.

# Database stuff
from db import db
from models.game_table import GameTable
from models.player import Player
from models.hand import Hand

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
                "hand_state": "won"|"lost"|"pending"|"tie"}
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
            game = GameTable(
                Player(
                    Hand(
                        BJ.draw_card(),
                        BJ.draw_card()
                    )
                ),
                Player(
                    Hand(
                        BJ.draw_card(),
                        BJ.draw_card()
                    ),
                )
            )

            db.session.add(game)
            db.session.commit()
            return {'username': get_jwt_identity(),
                    'player_hands': [
                        {
                            'first_card': 1,
                            'second_card': 2,
                            'third_card': 3,
                            'fourth_card': 4,
                            'fifth_card': 5
                        }
                    ],
                    'computer_hand': [{
                        'first_card': 1,
                        'second_card': 2,
                        'third_card': 3,
                        'fourth_card': 4,
                        'fifth_card': 5
                    }]}

            return get_jwt_identity()
        elif action == 'give_up':
            pass
        elif action == 'split':
            pass
        elif action == 'insure':
            pass
        elif action == 'stay':
            pass
        elif action == 'more':
            pass
        else:
            raise Exception("No valid action in json.")
