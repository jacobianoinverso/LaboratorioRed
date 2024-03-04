import matplotlib.pyplot as plt    #importamos los paquetes instalados en el entorno virtual para poder ejecutar el programa
import numpy as np
import seaborn as sns
import streamlit as st


n = st.text_input('Inserte el número de tiros n\n')             #pedimos al usuario los datos necesarios para calcular la distribución binomial
p = input ('Inserte la posibilidad de éxito p\n')
