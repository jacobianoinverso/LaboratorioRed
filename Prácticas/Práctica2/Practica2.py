import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ssτ
from scipy import special as ssp


st.title("Predicción de casos confirmados de COVID-19")

st.text("Basándose en datos obetnidos de los primeros casos, este programa permite predecir\naproximadamente cuándo tendrá un pico la pandemia y más o menos cuándo\nempezarán a disminuir los casos confirmados.")




conf_fecha = pd.read_csv('confirmados_fecha.csv',header=0)
conf_fecha = conf_fecha.loc[0:50]
print(conf_fecha)



def fit(x):
    A=  298.667
    u= 89.8887
    r =  8.41914
    x=x
    return A*math.exp(-((x-u)/r)**2/2)

fit = np.vectorize(fit)
value_range = np.arange(200)
fitfit= px.line(x=value_range, y=fit(value_range))
st.plotly_chart(fitfit)

fitfit.add_bar(x=conf_fecha.index, y=conf_fecha[4])

print(conf_fecha[4])