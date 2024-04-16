import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ssτ
from scipy import special as ssp


st.title("Predicción de casos confirmados de COVID-19")

st.write("Jacobo Ponce")
st.write("César García")

st.write("En este proyecto, haremos una prueba para saber qué tan acertado es aplicar la distribución binomial, de análisis probabilístico, para predecir la propagación de una enfermedad, tomando en cuenta los datos de las personas con resultados positivos para la prueba de covid-19.")
st.write("Tomaremos los datos de los casos confirmados en Guatemala en un periodo de tiempo inicial, haremos una predicción con el software GnuPlot y veremos qué tanto concuerda con los datos reales de los periodos siguientes de tiempo.")
st.write("Esto nos ayudará a entender si estos métodos son fiables para usarse en caso de haber enfermedades similares en el futuro o si tendremos que optar por métodos diferentes que represneten mejor la curva de contagios.")

st.title("Conceptos Generales")
st.header("Covid-19")
st.write("Mejor conocido como SRAS-CoV-2, que quiere decir coronavirus causante del síndrome respiratorio agudo severo de segundo tipo, es un tipo de coronavirus que, debido a su expansión a nivel mundial, porovocó una pandemia. Fue aislado por primera vez en Wuhan, China y se originó por un huesped animal.")
st.header("Distribución binomial")
st.write("Es el método de análisis estadístico que emplearemos en este trabajo.")
st.write("Con ayuda de ésta, podemos encontrar la probabilidad de un número de aciertos en n intentos de Bernopulli, donde cada uno de estos tiene una probabilidad p de éxito, donde p es un número entre 0 y 1 y consideramos también la variable q, la probabilidad de fracasos, que se expresa como q=1-p.")
st.header('Fórmulas relevantes:')
st.text('Distribución binomial:')
st.latex(r'''P_b(x) = \binom{n}{x}\frac{n!}{x!(n-x)!}''')
st.text('Donde x es el número de éxitos en cada caso. n, el número de tiros y p, la probabilidad de éxito de cada caso aislado.')
st.text('\n\nMedia de la distribución binomial:')
st.latex(r'''np''')

st.title("Planteamiento del problema")
st.write("A simples rasgos, podemos pensar en la expansión de una enfermedad como una binomial invertida; se empieza con pocos, casi nulos casos confirmados, luego existe un crecimiento exponencial, llega a un pico de casos y, conforme la gente va falleciendo o se va recuperando, la cantidad de casos va disminuyendo. Es por eso que hemos optado por intentar hacer una predicción de estos datos usando una distribución binomial, ya que en esta, conforme aumenta el número de éxitos, aumenta exponencialmente la probabilidad hasta llegar a un pico, para después disminuir.")
st.write("Como no estaremos trabajando con probailidades y éxitos, haremos los ejes de la gráfica de la siguiente forma: en el eje x, que tradicionalmente es para el número de éxitos, vamos a representar las fechas en orden. En el eje y, que tradicionalmente se usa para representar la probabilidad, vamos a representar el número de casos confirmados que hubo en cada día.")
st.writer("Una vez representados de esta forma estos datos, vamos a insertar nuestra lista de datos en el software de machine learning GnuPlot para que nos devuelva una predicción de esta curva. Con esta predicción, podremos saber aproximadamente cuándo tendremos un pico de casos y en qué fechas aproximadamente irá disminuyendo el número diario de contagios.")












conf_fecha = pd.read_csv('confirmados_fecha.csv')

conf_fecha = conf_fecha.loc[0:97
                            ]
conf_fecha = pd.DataFrame(conf_fecha)
print(conf_fecha)



def fit(x):
    A=  475.56
    u= 88.751 
    r =  6.43244
    x=x
    return A*math.exp(-((x-u)/r)**2/2)

fit = np.vectorize(fit)
value_range = np.arange(150
                        )
fitfit= px.line(x=value_range, y=fit(value_range))
fitfit.add_bar(x=conf_fecha.index, y=conf_fecha["confirmacion"])

st.plotly_chart(fitfit)


caldodepollo = pd.read_csv('confirmados_fecha.csv')

caldodepollo = caldodepollo.loc[0:384
                            ]
caldodepollo = pd.DataFrame(caldodepollo
)

caldoderes = px.line(x=value_range, y=fit(value_range))
caldoderes.add_bar(x=caldodepollo.index, y=caldodepollo["confirmacion"])

st.plotly_chart(caldoderes)

