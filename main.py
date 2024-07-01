import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv '
urlretrieve(url, 'datasets/global_covid_cases.csv')

df_covid = pd.read_csv('datasets/global_covid_cases.csv')

print(df_covid)
