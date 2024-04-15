import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ss



st.title("Predicción de casos confirmados de COVID-19")

st.text("Basándose en datos obetnidos de los primeros casos, este programa permite predecir aproximadamente cuándo tendrá un pico la pandemia y más o menos cuándo empezarán a disminuir los casos confirmados.")