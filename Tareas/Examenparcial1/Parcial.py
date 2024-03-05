import matplotlib.pyplot as plt    #importamos los paquetes instalados en el entorno virtual para poder ejecutar el programa
import numpy as np
import seaborn as sns
import streamlit as st

st.title('Graficadora de distribuciones binomiales')
st.write('He aquí una erramienta que permite representar de forma gráfica la cantidad de veces que un suceso tiene éxito.')


#Pedimos al usuario que inserte los valores de la distribución binomial

n = st.number_input('Inserte el número de tiros n\n', min_value=1, max_value=100, step=1, help='Insertar un valor entre 1 y 100"')      #pedimos al usuario los datos necesarios para calcular la distribución binomial

p = st.number_input('Inserte la posibilidad de éxito p\n', min_value=0.01, max_value=1.00, step=0.01, value=0.50, help='insertar un valor entre 0 y 1')

q=1-p 

DistBi = np.random.binomial(n=n,p=p,size=10)
st.write(DistBi)
