# Import flask dependencies
from flask import Blueprint, request
from flask_json import JsonError, json_response
from app.mod_predict_price.json_validation_classes import *
from app.mod_predict_price.models_ensemble import *
from app.mod_predict_price.models_ensemble import get_feature_array_from_json
from app.mod_predict_price.models_ensemble import get_histogram_from_json

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


@mod_price_predict.route('/plotData', methods=['POST'])
def plotting_data():
    inputs = ApiInputs(request)
    if not inputs.validate():
        return json_response(401, text=inputs.errors)

    inputs = PredictInputs(request)
    if not inputs.validate():
        return json_response(401, text=inputs.errors)

    hist, bin_edges = get_histogram_from_json(request.get_json())
    print(hist)
    print(bin_edges)
    return json_response(hist=hist.tolist(), bin_edges=bin_edges.tolist())


@mod_price_predict.route('/predict', methods=['POST'])
def predict_price():
    print(request.data)
    inputs = ApiInputs(request)
    if not inputs.validate():
        print(inputs.errors)
        return json_response(401, text=inputs.errors)

    inputs = PredictInputs(request)
    if not inputs.validate():
        print(inputs.errors)

        return json_response(401, text=inputs.errors)
    params = get_feature_array_from_json(request.get_json())

    predicted = get_prediction(params)

    return json_response(predicted_price=predicted)



