from flask_inputs import Inputs
from wtforms.validators import *
from flask_inputs.validators import JsonSchema


class PredictInputs(Inputs):
    json = {
        'area_meters': [DataRequired("area_meters data required"), NumberRange(0, 9999, message='Area should be number 0-9999')],
        'condition': [DataRequired("condition data required"), NumberRange(0, 3, message='Condition should be number 0-3')],
        'rooms': [DataRequired("rooms data required"), NumberRange(1, 999, message='Rooms should be number 0-999')],
        'build_year': [DataRequired("build_year data required"), NumberRange(0, 2100, message='Year should be between '
                                                                                        '0-2100')],
        'floor': [DataRequired("floor data required"), NumberRange(0, 999, message='Floor should be number 0-999')],

        'balcony': [AnyOf([1, 0])],
        'terrass': [AnyOf([1, 0])],
        'sauna': [AnyOf([1, 0])],
        'pool': [AnyOf([1, 0])],

        'house_material': [
            AnyOf(['None', 'betoonmaja', 'paneelmaja', 'kivimaja', 'palkmaja', 'plokkmaja', 'palk-kivimaja',
                   'puitmaja'])],
        'linnaosa': [
                     AnyOf(['None', 'Haabersti', 'Kadriorg', 'Kesklinn', 'Kristiine', 'Lasnamäe', 'Mustamäe', 'Nõmme',
                            'Pirita', 'Põhja-Tallinn', 'Vanalinn'])],
        'energy_class': [
                         AnyOf(['None', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])],

        'heating': [
                    AnyOf(['None', 'elektriküte', 'gaasiküte', 'ahjuküte', 'maaküte', 'autnoomne küte', 'tahkekütus',
                           'keskküte', 'õhksoojuspump', 'kamin', 'põrandaküte', 'kombineeritud küte'])],
    }


def get_valid_json_schema():
    valid_schema = {
                'type': 'object',
                'properties': {
                    'area_meters': {'type': 'number'},
                    'condition': {'type': 'number'},
                    'rooms': {'type': 'number'},
                    'build_year': {'type': 'number'},
                    'floor': {'type': 'number'},
                    'balcony': {'type': 'number'},
                    'terrass': {'type': 'number'},
                    'sauna': {'type': 'number'},
                    'pool': {'type': 'number'},
                    'house_material': {'type': 'string'},
                    'linnaosa': {'type': 'string'},
                    'energy_class': {'type': 'string'},
                    'heating': {'type': 'array'}
                }
    }
    return valid_schema


class ApiInputs(Inputs):
    json = [JsonSchema(schema=get_valid_json_schema())]




