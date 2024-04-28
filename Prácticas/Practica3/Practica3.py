import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ssτ
from scipy import special as ssp

st.title('Decaimiento radioactivo del Cesio-137')
st.write("Jacobo Ponce")
st.write("César García")

st.write("En este experimento, vamos a analizar la cantidad de partículas en el aire y las emitidas por una muestra de cesio-137 en decadencia y vamos a ajustar los resultados utilizando las distribuciones de Gauss y de Poisson. Para saber si estos ajustes son correctos, haremos la prueba de χ² para cada uno de los ajustes. Esto nos va a ayudar a saber si las funciones con las que vamos a ajustar los datos pueden ser usadas para estudiar el decaimiento radioactivo o si vamos a tener que optar por una distribución diferente para poder estudiar estos datos.")

st.title("Conceptos generales")
st.header("Isótopos radiactivos")
st.write("También llamados radioisótopos, entre otros nombres, son átomos que tienen un exceso de energía, lo que los vuelve inestables. Esta energía se discipa de tres maneras; puede emitirse desde el núcleo (radiación γ), puede transferirse a uno de sus electrones para ser liberado como un electrón de conversión interna o puede ser usada para crear y emitir una partícula nueva (llamada partícula α ο β).")
st.write("Los radioisótopos se representan con el nombre del elemento, acompañado del número total de protones y neutrones en su núcleo.")
st.write("El isótopo que estudiaremos hoy, el cesio-137, recibe su nombre del hecho de que su núcleo se conforma ed 55 protones y 82 neutrones.")

st.header("Cesio-137")
st.write("Es uno de los isótopos más estables de cesio. Se obtiene de forma sintética a partir de fisión nuclear. El Cesio-137 es un emisor beta, el 94,6 por ciento se desintegra en Ba-137m y el resto directamente en Ba-137 que es estable. La energía de los fotones de Ba-137m es 661,7 keV. Estos fotones pueden ser utilizados en la irradiación de los alimentos, o de la radioterapia en el cáncer. Cs-137 es menos utilizado para la radiografía industrial que otros isótopos gamma. Se puede encontrar en algunos medidores de humedad y de densidad, medidores de flujo, sensores y otros equipos.")

st.header("Decaimiento radiactivo")
st.write("Es la reducción del núcleo de un isótopo inestable en una muestra de materia en un periodo de tiempo que varía de isótopo a isótopo. Toma lugar hasta que toda la sustancia se convierte en algún elemento más estable")

st.header("Distribución Gaussiana")
st.write("También llamada distribución normal, es una distribución probabilística de variable continua simétrica con respecto a un parámetro. Por ls forma acampanada de su función de densidad, se le suele llamar campana de Gauss. Es ampliamente usada porque permite modelar diversos fenómenos incluso de ramas de estudio diferentes.")
st.header("Fórmulas relevantes")
st.write("Densidad de probabilidad")
st.latex(r'''pdf = \frac{1}{\sigma\sqrt{2\pi}}''')