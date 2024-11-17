import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-energy-data.csv')
df_countries = df['country'].drop_duplicates()
df_years = df['year'].drop_duplicates().sort_values(ascending=False)
st.markdown('### Distribución de energía')

countries = st.selectbox(
    'País o agrupación a comparar.',
    df_countries,
    placeholder='Seleccione un elemento'
)

years = st.selectbox(
    'Año a visualizar.',
    df_years,
    placeholder='Seleccione un año'
)

df_graph = df[
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
k = df_graph[(df_graph['country']==countries) & (df_graph['year']==years)].index.values[0]
df_graph = df_graph.drop(['country', 'year', 'fossil_electricity', 'renewables_electricity', 'low_carbon_electricity'], axis=1)
df_graph = df_graph.transpose()
df_graph['index1'] = ['Biocombustibles', 'Carbón', 'Gas', 'Hídrica', 'Núclear', 'Petróleo', 'Solar', 'Eólica']

#df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(names=df_graph['index1'],values=df_graph[k], title='Distribución de energía')

st.plotly_chart(fig)
