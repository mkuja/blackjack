
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_current_user  # Only identified players may play.

# Database stuff
from ..db import db
from ..models.game_table import GameTable
from ..models.player import Player
from ..models.hand import Hand


class Play(Resource):

    @jwt_required
    def post(self):
        """JSON should be of format:

            {"action": "more"|"stay"|"insure"|"split"|"give_up"|"new_game"}


            With all actions the reply will be like:

            {"username": username,
            "hands": [
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
            return get_current_user()
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
