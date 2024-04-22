import matplotlib.pyplot as plt    #importamos los paquetes instalados en el entorno virtual para poder ejecutar el programa
import numpy as np
import seaborn as sns
import streamlit as st
from scipy import stats as sts
from scipy.stats import binom
st.title('Graficadora de distribuciones binomiales')
st.write('He aquí una herramienta que permite representar de forma gráfica la probabilidad de que un suceso tenga éxito en repetidas ocasiones.')


#Pedimos al usuario que inserte los valores de la distribución binomial

n = st.number_input('Inserte el número de tiros n\n', min_value=1, max_value=100, step=1, help='Insertar un valor entre 1 y 100"')      #pedimos al usuario los datos necesarios para calcular la distribución binomial

p = st.number_input('Inserte la posibilidad de éxito p\n', min_value=0.01, max_value=1.00, step=0.01, value=0.50, help='insertar un valor entre 0 y 1')

x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)  
plt.bar(x, pmf)  
plt.xlabel('Number of Heads')  
plt.ylabel('Probability')  
plt.title('Binomial Distribution - Coin Flips')  
plt.show()  