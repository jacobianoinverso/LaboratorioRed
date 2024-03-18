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








st.header('Distribución de tiros de monedas')

st.write('Con ayuda de este programa, usted podrá ver los datos de 100 tiros de 10 monedas ajustarse a una distribución binomial.')

st.markdown("[Más información.](#Marco-teórico)")

st.markdown("[¿Cómo funciona?](#Diseño-Experimental)")




m = st.slider('Elija el número de tiros para graficar la distribución',1,100)

def binom(x,n,p):
    # print('binom(',x,n,p,')')
    
    x = int(x)
    n = int(n)
        
    comb = math.comb(n,x)
    p_x = p**x
    q_nx = (1-p)**(n-x)

    return comb*p_x*q_nx
    # return A * scs.binom.pmf(x,n,p)

binom = np.vectorize(binom)


data = pd.read_csv('fichas.csv')
print(f'data:\n{data}')

data = data.loc[:m]

counts_non_sort = data['JC'].value_counts()
counts = pd.DataFrame(np.zeros(11))
# print(counts)

for row, value in counts_non_sort.items():
    counts.loc[row,0] = value

print(f'counts:\n{counts}')
print(f'index: {counts.index.values}')
print(f'normalized counts: {list(counts[0]/m)}')


fit, cov_mat = sco.curve_fit(binom,counts.index.values,counts[0]/m,[10,0.5],bounds=[(0,0),(np.inf,1)])

print(f'Fit:\n{fit}\ncov_mat\n{cov_mat}')

n = fit[0]
p = fit[1]

print(f'Este es el valor de n: {n}\nEste es el valor de p: {p}')




binomial_plot = px.line(x=counts.index.values, y=binom(counts.index.values,n,p), title="Lanzamiento de fichas")

binomial_plot.add_bar(x=counts.index.values, y=counts[0]/m, name='Lanzamientos experimentales')

st.write(binomial_plot)



advanced = str(m)


st.text('Conteo medio observado para ' + advanced + ' tiros')



chess = sum(data['JC'])/(m+1)
battle = round(chess, 2)
advanced2 = str(battle)

Culito = np.std(data['JC'])
hediondo = round(Culito, 2)
Caca = str(hediondo)



st.text(advanced2 + '±' + Caca)


st.text('Conteo medio teórico')

estoscelos = 10/2

mehacen = np.sqrt(10*(1/2**2))

dañome = str(estoscelos)

jamasaprende = round(mehacen,2)

enloquecen = str(jamasaprende)

st.text(dañome + '±' + enloquecen)





st.title('Distribución para 600 tiros de 10 monedas')




 #Grafica 1
#
#
#
#

t = 600

def binom(aa,df,gh):
    # print('binom(',x,n,p,')')
    #aa = x, df = n, gh = p, hg = q
    aa = int(aa)
    df = int(df)
        
    comb = math.comb(df,aa)
    gh_aa = gh**aa
    hg_dfaa = (1-gh)**(df-aa)

    return comb*gh_aa*hg_dfaa
    # return A * scs.binom.pmf(x,n,p)

binom = np.vectorize(binom)


data = pd.read_csv('fichas.csv')
print(f'data:\n{data}')

counts_non_sort = data['JC'].value_counts()
counts = pd.DataFrame(np.zeros(11))
# print(counts)

for row, value in counts_non_sort.items():
    counts.loc[row,0] = value

print(f'counts:\n{counts}')
print(f'index: {counts.index.values}')
print(f'normalized counts: {list(counts[0]/t)}')


fit2, cov_mat2 = sco.curve_fit(binom,counts.index.values,counts[0]/t,[10,0.5],bounds=[(0,0),(np.inf,1)])

print(f'Fit:\n{fit}\ncov_mat\n{cov_mat}')

df = fit[0]
gh = fit[1]

print(f'Este es el valor de n: {df}\nEste es el valor de p: {gh}')




binomial_plot2 = px.line(x=counts.index.values, y=binom(counts.index.values,n,p), title="Lanzamiento de fichas")

binomial_plot2.add_bar(x=counts.index.values, y=counts[0]/t, name='Lanzamientos experimentales')

st.write(binomial_plot2)


st.text('Conteo medio observado para 600 tiros')

arremangala = sum(data['JC'])/600

arrempujala = round(arremangala,2)

Arremangala = str(arrempujala)

Arrempujala = np.std(data['JC'])

arremángala = round(Arrempujala,2)

arrempújala = str(arremángala)

st.text(Arremangala + '±' + arrempújala)

st.text('Conteo medio teórico para 600 tiros')

ylachonasemueve = 10/2

ylagentelegrita = str(ylachonasemueve)

nohaymejorquelachona = np.sqrt(10*(1/2**2))

paralaquebradita = round(nohaymejorquelachona, 2)

aaaaaaaaaaaaa = str(paralaquebradita)

st.text(ylagentelegrita + '±' + aaaaaaaaaaaaa)





#Grafica 2 
#
#
#
#


st.title('Conceptos básicos:', anchor = 'Marco-teórico')

st.title('Diseño Experimental', anchor = 'Diseño-Experimental')





