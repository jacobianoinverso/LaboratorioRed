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









st.header("Distribución Gaussiana")
st.write("También llamada distribución normal, es una distribución probabilística de variable continua simétrica con respecto a un parámetro. Por ls forma acampanada de su función de densidad, se le suele llamar campana de Gauss. Es ampliamente usada porque permite modelar diversos fenómenos incluso de ramas de estudio diferentes.")
