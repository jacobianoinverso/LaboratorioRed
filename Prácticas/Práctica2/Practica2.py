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
    background-image: url("https://cloudfront-us-east-1.images.arcpublishing.com/gruponacion/LEBXCHHCNJFMNBOYLMZJ4RJYQM.jpg");
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


st.markdown("Θέλω μία πόρνη")