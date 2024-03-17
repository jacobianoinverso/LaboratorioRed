import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ss


background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://cdn-p.smehost.net/sites/a8928da38df6414aae98564041b07ae0/wp-content/uploads/2016/09/Vicente-Fernandez-Header-1920x964.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


input_style = """
<style>
input[type="text"] {
    background-color: transparent;
    color: #a19eae;  // This changes the text color inside the input box
}
div[data-baseweb="base-input"] {
    background-color: transparent !important;
}
[data-testid="stAppViewContainer"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(input_style, unsafe_allow_html=True)




st.title('Distribución de tiros de monedas')

m = st.slider('Elija el número de tiros para graficar la distribución',1,100)

aa = data.loc[:m,'JC']

plt.hist(x=aa, bins=intervalos, color='#F2AB6D', rwidth=0.85)
plt.title('Histograma de tiros de monedas')
plt.xlabel('Cantidad de caras')
plt.ylabel('Cantidad de veces')
plt.xticks(range(1,10))

st.pyplot()

data = pd.read_csv("fichas.csv")
# data.loc[:m,'JC']
print(f'data:\n{data}')

fitted_results = ss.fit(ss.binom,data,bounds=[(0,100),(0,1)])
print(fitted_results)
fitted_results.plt()
st.pyplot()




