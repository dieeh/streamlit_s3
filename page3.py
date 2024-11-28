import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-energy-data.csv').fillna(0) # se lee el dataframe y se reemplazan los NaN con ceros

st.markdown('### Distribución de energía')

countries = st.selectbox(
    'País o agrupación a comparar.',
    df['country'].drop_duplicates(),
    placeholder='Seleccione un elemento'
)

years = st.selectbox(
    'Año a visualizar.',
    df[df['country']==countries]['year'].drop_duplicates().sort_values(ascending=False),
    placeholder='Seleccione un año'
)

df_graph = df[ # se vuelve a filtrar el dataframe
    ['country',
     'year',
     'biofuel_electricity',
     'coal_electricity',
     'fossil_electricity',
     'gas_electricity',
     'hydro_electricity',
     'low_carbon_electricity',
     'nuclear_electricity',
     'oil_electricity',
     'renewables_electricity',
     'solar_electricity',
     'wind_electricity'
    ]
]
df_graph = df_graph[(df_graph['country']==countries) & (df_graph['year']==years)]
df_graph = df_graph.drop(['country', 'year', 'fossil_electricity', 'renewables_electricity', 'low_carbon_electricity'], axis=1)
k = df_graph.index.values[0]
df_graph = df_graph.transpose()
df_graph['index1']=['Energía por biocombustibles', 'Energía por carbón', 'Energía por gas', 'Energía hídrica', 'Energía nuclear', 'Energía por petróleo', 'Energía solar', 'Energía eólica']

# Se filtra y se eliminan columnas del df, se guarda el index de la busqueda y se transpone
# para que los valores queden en una columna. Luego se añade una columna con nombres, para el grafico

fig = px.pie(
    names=df_graph['index1'],
    values=df_graph[k],
    title='Distribución de energía',
    hole=0.35 # hole hace que el grafico sea una dona
)

st.plotly_chart(fig)
