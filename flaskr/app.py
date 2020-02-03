from flask import Flask, render_template
from flask_jwt import JWT, jwt_required

from flaskr.security import authenticate, identity


app = Flask(__name__, static_folder="build/static", template_folder="build")
app.secret_key = 'test'

app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)


jwt = JWT(app, authenticate, identity)

@app.route("/")
def hello():
    return render_template('index.html')

app.debug=True
app.run(host='0.0.0.0')