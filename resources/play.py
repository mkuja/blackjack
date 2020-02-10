
from flask_restful import Resource, reqparse
# from ..models.user import User as UserModel
# from ..db import db
from flask_jwt import jwt_required, current_identity


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
        raise Exception("Play.post")
        return {"jeejee": "joojoo"}, 200
