import numpy as arzu
import pandas as pa
import streamlit as st
import scipy as spicy

page_bg_img = '''
<style>
body {
background-image: url("https://cdn-p.smehost.net/sites/a8928da38df6414aae98564041b07ae0/wp-content/uploads/2016/09/Vicente-Fernandez-Header-1920x964.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Distribución de 100 tiros de monedas advanced')
