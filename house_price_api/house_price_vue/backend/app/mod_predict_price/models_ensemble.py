from app.model_classes import StackingAveragedModels
from sklearn.externals import joblib
import pandas as pd
import numpy as np

xgb_model = joblib.load(open("../models/xgb_model.pkl", "rb"))
stacked_model = joblib.load(open("../models/stacked_model.pkl", "rb"))

sample = pd.read_csv("../models/sample_data.csv")

raw_data = pd.read_csv("../models/city24_processed.csv")


def map_heating(heating_num):
    heating_map = {0:'keskküte', 1:'elektriküte', 2:'gaasiküte', 3:'ahjuküte', 4:'maaküte', 5:'autnoomne küte', 6:'tahkekütus',
                   7:'õhksoojuspump', 8:'kamin', 9:'põrandaküte', 10:'kombineeritud küte'}
    return heating_map


def get_prediction(feature_array):
    feature_array = np.array(feature_array)
    xgb = xgb_model.predict(feature_array)
    stacked = stacked_model.predict(feature_array)

    xgb = np.expm1(xgb)
    stacked = np.expm1(stacked)
    return stacked * 0.70 + xgb * 0.3


def get_feature_array_from_json(json):
    df_row = sample.copy()
    area_m = np.log(float(json['area_meters']))
    df_row['üldpind'] = area_m
    df_row['rõdu'] = json['balcony']
    df_row['seisukord'] = json['condition']
    df_row['tubade_arv'] = json['rooms']

    df_row[json['linnaosa']] = 1

    df_row['terrass'] = json['terrass']

    for heating in json['heating']:
        df_row[heating] = 1

    df_row[json['house_material']] = 1

    energy_prefix = 'energy_class_'
    enrgy_class = energy_prefix + str(json['energy_class'])
    df_row[enrgy_class] = 1
    df_row['korrus'] = json['floor']
    df_row['saun'] = json['sauna']
    df_row['bassein'] = json['pool']
    build_year = int(json['build_year'])
    build_year_prefix = 'ehitusaasta_'
    if not build_year < 1699 or not build_year > 2020:
        build_year_col = build_year_prefix + str(build_year)
        df_row[build_year_col] = 1
    return df_row.values


def get_histogram_from_json(json):
    has_criteria_2 = (json['area_meters'] + json['area_meters'] * 0.2) > raw_data['üldpind']
    has_criteria_2_2 = (json['area_meters'] - json['area_meters'] * 0.2) < raw_data['üldpind']
    has_criteria_3 = raw_data['rõdu'] == json['balcony']
    has_criteria_4 = raw_data['seisukord'] == json['condition']
    has_criteria_6 = raw_data[json['linnaosa']] == 1
    has_criteria_7 = raw_data['terrass'] == json['terrass']
    has_criteria_9 = raw_data[json['house_material']] == 1
    has_criteria_10 = raw_data['korrus'] == json['floor']
    has_criteria_11 = raw_data['bassein'] == json['pool']

    data = raw_data[has_criteria_2 & has_criteria_2_2 & has_criteria_4
        & has_criteria_6]['hind'].values

    return np.histogram(data, bins=18, density=False)


def init_sample_data():
    sample.drop(['id', 'hind'], axis=1, inplace=True)
    for col in sample.columns:
        sample[col] = 0


init_sample_data()
