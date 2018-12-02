# Import flask and template operators
from flask import Flask, render_template, jsonify
from flask_json import FlaskJSON
from flask_cors import CORS
import requests

# Define the WSGI application object
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

json = FlaskJSON(app)

# Configurations
app.config.from_object('config')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_predict_price.controllers import mod_price_predict as price_predict
# Register blueprint(s)
app.register_blueprint(price_predict)


