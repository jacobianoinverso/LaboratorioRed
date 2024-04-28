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

st.write("En este experimento, vamos a analizar la cantidad de partículas en el aire y las emitidas por una muestra de cesio-137 en decadencia y vamos a ajustar los resultados utilizando las distribuciones de Gauss y de Poisson. Para saber si estos ajustes son correctos, haremos la prueba de χ² para cada uno de los ajustes.")