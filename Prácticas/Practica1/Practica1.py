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

data = pd.read_csv("fichas.csv")
data = data.loc[:m,'JC']
print(f'data:\n{data}')

fitted_results = ss.fit(ss.binom,data,bounds=[(0,100),(0,1)])
print(fitted_results)
fitted_results.plot()
st.pyplot()




fig = plt.figure(figsize=(8,8))
plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=100, c='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=100, c='red', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=100, c='yellow', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=100, c='black', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=100, c='blue', label='Cluster 5')
plt.legend()
plt.title('Customer Groups')
plt.xlabel('Income')
plt.ylabel('Spending Score')
st.pyplot(fig) # instead of plt.show()