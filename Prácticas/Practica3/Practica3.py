import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import optimize as sco
import math
import plotly.express as px
from scipy import stats as ssτ
from scipy import special as ssp
from scipy.stats import poisson

st.title('Decaimiento radioactivo del Cesio-137')
st.write("Jacobo Ponce")

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
st.latex(r'''pdf = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}''')
st.write("Función de distribución de probabilidad")
st.latex(r'''cdf=\frac{1}{2}\left[1+erf\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]''')


st.header("Distribución de Poisson")
st.write("Es una distribución de probabilidad discreta que representa la probabilidfad de que suceda una cierta cantidad de eventos dentro de un intervalo de tiempo.")
st.header("Fórmulas relevantes")
st.write("Función de probabilidad")
st.latex(r'''fp=\frac{e^{-\lambda}\lambda^k}{k!}''')

st.write("Función de distribución")
st.latex(r'''cdf = \frac{\Gamma(\lfloor k+1\rfloor,\lambda)}{\lfloor k\rfloor!}''')
st.write("Donde Γ(x,y) es la función gamma incompleta")

st.header("Prueba de χ²")

st.write("Esta prueba se refiere a tres tipos diferentes de pruebas estadísticas. En este caso, vamos a estar tratando la prueba de Pearson para saber si los ajustes son los correctos según los datos para los que se vayan a usar.")
st.write("La prueba de Pearson consiste en hacer dos hipótesis y si el valor de χ cuadrado es mayor o menor parámetro, se considera verdadera cualquiera de las dos hipótesis. Tanto las hipótesis como el parámetro van a variar edpendiendo del experimento.")
st.title("Fórmulas relevantes")

st.write("Fórmula de distribución de probabilidad de Pearson")
st.latex(r'''\chi^2=\sum^{k}_{i=1}\frac{(x_i-m_i)^2}{m_i}=\sum^k_{i=1}\frac{x_i^2}{m_i}-n''')

st.title("Planteamiento del problema")
st.write("Las partículas elementales que se desprenden de diferentes fenómenos como el decaimiento radioactivo, tienen normalmente un comportamiento que a simple vista pareciera ser caótico. Cuando tenemos como muestra un radioisótopo, la fuente de partículas es más constante. Sin embargo, cuando tenemos como muestra un espacio cualquiera, pueden ser partículas emitidas por estrellas lejanas, por radioisótopos en otras partes del mundo, por fenómenos cósmicos de alta energía, etcétera, por lo que la fuente de partículas se podría considerar más aleatoria.")
st.write("Vamos a estudiar las detecciones de partículas tanto de un espacio cualquiera de aire como de un radioisótopo para vcerificar si estas emisiones son realmente aleatorias o si siguen un patrón que podemos ajustar a alguna de las dos distribuciones descritas con anterioridad.")

st.title("Medición de los datos")
st.write("Usando un detector de partículas de diversos niveles de energía, haremos 250 mediciones en un espacio de aire, donde pensamos que la cantidad de partículas va a ser más aleatoria. Luego, haremos 250 mediciones sobre una muestra de cesio-137, donde pensamos que las emisiones van a tener un orden más visible.")
st.write("Una vez obtenidos estos datos, los ordenaremos en gráficas separadas para ver si hay cierta relación entre los datos y una curva conocida.")
st.write("Ajustaremos las gráficas a dos funciones de análisis probabilístico; la distribución normal o Gaussiana y la distribución de Poisson.")
st.write("Una vez graficados los datos junto a los ajustes, haremos la prueba de χ cuadrado, donde nuestro parámetro va a ser el número máximo              . Si el resultado de la prueba es menor a este parámetro, vamos a considerar que la distribución ajustada describe de forma acertada la probabilidad de la cantidad de partículas emitidas. De ser mayor, vamos a considerar de que no la describe de forma completa.")


st.title("Resultados")

st.write("A continuación, vemos la tabla de resultados de la cantidad de partículas medidas en un espacio cualquiera de aire ajustados con una distribución gaussiana")
aigre2 = pd.read_csv('chuchitosdeaire.csv')
aigre = aigre2.value_counts().sort_index().reset_index()
aigre.columns = ['value', 'count']
def fitaire(x, A, u, r):
    return A * np.exp(-((x - u) / r)**2 / 2)
guess = (1025.07, -305.742, 91.8277)
params, _ = sco.curve_fit(fitaire, aigre['value'], aigre['count'], p0=guess)
value_range = np.arange(aigre['value'].min(), aigre['value'].max() + 1)
fig = px.bar(x=aigre['value'], y=aigre['count'], labels={'x': 'Value', 'y': 'Count'}, title='Histograma de Valores')
fig.add_scatter(x=value_range, y=fitaire(value_range, *params), mode='lines', name='Curva ajustada')
st.plotly_chart(fig)

st.write("Estos son los mismos datos, pero ajustados a la distribución de Poisson")


def load_data(file_path):
    return pd.read_csv(file_path, header=None, names=['data'])
data = load_data("chuchitosdeaire.csv")

# Estimar la distribución Poisson
mu = data['data'].mean()
poisson_dist = poisson(mu)
x = np.arange(0, data['data'].max() + 1)
pmf = poisson_dist.pmf(x)

# Crear un gráfico combinado
fig, ax = plt.subplots(figsize=(8, 6))

# Gráfico de barras de los datos originales
ax.bar(data['data'].value_counts().sort_index().index, data['data'].value_counts().sort_index().values, label='Datos originales')
ax.set_xlabel("Valor")
ax.set_ylabel("Frecuencia")
ax.set_title("Gráfico de barras de los datos originales")

# Gráfico de la distribución Poisson estimada
ax.plot(x, 250*pmf, 'ro-', label='Distribución Poisson estimada')
ax.set_xlabel("Valor")
ax.set_ylabel("Probabilidad")

# Agregar leyenda
ax.legend()

# Mostrar gráfico
st.pyplot(fig)


st.write("A continuación, los datos de las partículas emitidas por el cesio-137 ajustadas con la distribución gaussiana")



guate = pd.read_csv('chuchitosdecesio.csv')

morfosis = guate.value_counts().sort_index().reset_index()
morfosis.columns = ['value', 'count']

def fitgaussian(x, A, mu, sigma):
    return A * np.exp(-0.5 * ((x - mu) / sigma)**2)

carnitas = (3000, 450, 50)

paramsa, _ = sco.curve_fit(fitgaussian, morfosis['value'], morfosis['count'], p0=carnitas)

value_range2 = np.linspace(morfosis['value'].min(), morfosis['value'].max(), 1000)

fig = px.bar(x=morfosis['value'], y=morfosis['count'], labels={'x': 'Value', 'y': 'Count'}, title='Histograma de Valores')
fig.add_scatter(x=value_range2, y=fitgaussian(value_range2, *paramsa), mode='lines', name='Curva ajustada')

st.plotly_chart(fig)

st.write("Y a continuación, los datos del cesio pero ajustados con la distribución de Poisson")

data = load_data("chuchitosdecesio.csv")

# Estimar la distribución Poisson
mu = data['data'].mean()
poisson_dist = poisson(mu)
x = np.arange(0, data['data'].max() + 1)
pmf = poisson_dist.pmf(x)

# Crear un gráfico combinado
fig, ax = plt.subplots(figsize=(8, 6))

# Gráfico de barras de los datos originales
ax.bar(data['data'].value_counts().sort_index().index, data['data'].value_counts().sort_index().values, label='Datos originales')
ax.set_xlabel("Valor")
ax.set_ylabel("Frecuencia")
ax.set_title("Gráfico de barras de los datos originales")

# Gráfico de la distribución Poisson estimada
ax.plot(x, 250*pmf, 'ro-', label='Distribución Poisson estimada')
ax.set_xlabel("Valor")
ax.set_ylabel("Probabilidad")

# Agregar leyenda
ax.legend()

# Mostrar gráfico
st.pyplot(fig)