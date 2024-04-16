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

st.write("Jacobo Ponce\nCésar García")

st.write("En este proyecto, haremos una prueba para saber qué tan acertado es aplicar la distribución binomial, de análisis probabilístico, para predecir la propagación de una enfermedad, tomando en cuenta los datos de las personas con resultados positivos para la prueba de covid.19.")




conf_fecha = pd.read_csv('confirmados_fecha.csv')

conf_fecha = conf_fecha.loc[0:97
                            ]
conf_fecha = pd.DataFrame(conf_fecha)
print(conf_fecha)



def fit(x):
    A=  475.56
    u= 88.751 
    r =  6.43244
    x=x
    return A*math.exp(-((x-u)/r)**2/2)

fit = np.vectorize(fit)
value_range = np.arange(150
                        )
fitfit= px.line(x=value_range, y=fit(value_range))
fitfit.add_bar(x=conf_fecha.index, y=conf_fecha["confirmacion"])

st.plotly_chart(fitfit)


