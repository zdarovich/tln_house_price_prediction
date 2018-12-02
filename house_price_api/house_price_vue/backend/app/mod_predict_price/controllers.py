# Import flask dependencies
from flask import Blueprint, request
from flask_json import JsonError, json_response
from random import *
from mod_predict_price.json_validation_classes import *
from mod_predict_price.models_ensemble import *
from mod_predict_price.models_ensemble import get_feature_array_from_json
import numpy as np

mod_price_predict = Blueprint('price_predict', __name__, url_prefix='/api')


@mod_price_predict.route('/increment', methods=['POST'])
def increment_value():
    # We use 'force' to skip mimetype checking to have shorter curl command.
    data = request.get_json(force=True)
    try:
        value = int(data['value'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(value=value + 1)


@mod_price_predict.route('/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return json_response(response)


@mod_price_predict.route('/predict', methods=['POST'])
def predict_price():
    inputs = ApiInputs(request)
    if not inputs.validate():
        return json_response(401, text=inputs.errors)

    inputs = PredictInputs(request)
    if not inputs.validate():
        return json_response(401, text=inputs.errors)
    params = get_feature_array_from_json(request.get_json())

    predicted = get_prediction(params)

    return json_response(predicted_price=predicted)



