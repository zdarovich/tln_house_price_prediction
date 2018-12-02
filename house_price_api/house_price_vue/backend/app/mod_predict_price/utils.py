import numpy as np


def get_feature_array_from_json(json):
    return np.array([
        json['area_meters'],
        json['condition'],
        json['rooms'],
        json['build_year'],
        json['floor'],
        json['balcony'],
        json['terrass'],
        json['sauna'],
        json['pool'],
        json['house_material'],
        json['linnaosa'],
        json['energy_class'],
        json['heating']
    ])
