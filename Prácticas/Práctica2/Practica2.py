import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ssτ



st.title("Predicción de casos confirmados de COVID-19")

st.text("Basándose en datos obetnidos de los primeros casos, este programa permite predecir\naproximadamente cuándo tendrá un pico la pandemia y más o menos cuándo\nempezarán a disminuir los casos confirmados.")




conf_fecha = pd.read_csv('confirmados_fecha.csv',header=0)
conf_fecha = conf_fecha.loc[0:50]
print(conf_fecha)



def binom(x,n,p):
    print('binom(',x,n,p,')')
    
    # x = int(x)
    # n = int(n)
        
    comb = ssp.comb(n,x)
    p_x = p**x
    q_nx = (1-p)**(n-x)

    return comb*p_x*q_nx
    # return A * scs.binom.pmf(x,n,p)

fit, cov_mat = sco.curve_fit(binom,conf_fecha.index.values,conf_fecha['sintomas'],bounds=[(0,0),(np.inf,1)],p0=[200,0.8])

print(f'Fit:\n{fit}\ncov_mat\n{cov_mat}')

n = fit[0]
p = fit[1]

print(f'Este es el valor de n: {n}\nEste es el valor de p: {p}')




binomial_plot = px.line(x=conf_fecha.index.values, y=binom(conf_fecha.index.values,n,p), title="Lanzamiento de fichas")

binomial_plot.add_bar(x=conf_fecha.index.values, y=conf_fecha['sintomas']/conf_fecha['sintomas'].sum(), name='Lanzamientos experimentales')

binomial_plot.show()