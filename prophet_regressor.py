import pickle
import numpy as np 
import pandas as pd 
pd.set_option('display.float_format', '{:.6f}'.format)

import datetime
import math
from math import sqrt

from prophet import Prophet
from prophet.plot import add_changepoints_to_plot
from sklearn.metrics import mean_squared_error

def read_pickle(file):
    # Load the model from a file
    with open(file, 'rb') as file:
        model = pickle.load(file)

    return model

def prepare_regressor(file):
    regressor = pd.read_csv(file, sep=';')
    regressor['dt'] = pd.to_datetime(regressor['dt'], format='%d/%m/%Y') + pd.offsets.MonthEnd(0)
    regressor = regressor.set_index('dt').fillna(0)

    regressor['keb_ppkm4'] = 0
    regressor.loc[['2021-07-31','2021-08-31'],'keb_ppkm4'] = 1

    regressor['keb_ppkm3'] = 0
    regressor.loc[['2022-02-28'],'keb_ppkm3'] = 1

    regressor['keb_ppkm_mikro'] = 0
    regressor.loc[['2021-02-28','2021-03-31','2021-04-30','2021-05-31'],'keb_ppkm_mikro'] = 1

    regressor['awal_covid'] = 0
    regressor.loc[['2020-01-31','2020-02-29','2020-03-31','2020-04-30','2020-05-31','2020-06-30'],'awal_covid'] = 1

    regressor['pandemi'] = 0
    regressor.loc[(regressor.index >= '2020-01-01'), 'pandemi'] = 1

    regressor['after_pandemi'] = 0
    regressor.loc[(regressor.index >= '2023-07-01'), 'after_pandemi'] = 1

    return regressor

def predict(model, regressor):
    future = model.make_future_dataframe(periods=6, freq='ME')
    future = future.set_index('ds')
    future[['idul_fitri','cuti_idul_fitri','libur_sekolah','jumlah_libur','keb_ppkm4','keb_ppkm3','keb_ppkm_mikro','pandemi','awal_covid','after_pandemi']] = regressor[['idul_fitri','cuti_idul_fitri','libur_sekolah','jumlah_libur','keb_ppkm4','keb_ppkm3','keb_ppkm_mikro','pandemi','awal_covid','after_pandemi']]
    future = future.reset_index()

    future.loc[future.ds == '2024-01-31','libur_sekolah'] = 1
    forecast = model.predict(future)
    
    return(forecast)


def main():
    file_pickle = 'model/prophet_regressor.pkl'
    file_regressor = 'data/regressor.csv'
    model = read_pickle(file_pickle)
    regressor = prepare_regressor(file_regressor)
    print('++ read file done ++')

    forecast = predict(model, regressor)
    print('++ forecaasting done ++')
    print(forecast.iloc[-6:,].yhat)

# This code block ensures that the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()