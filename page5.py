import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-energy-data.csv').fillna(0)
df = df[['country', 'year', 'iso_code', 'low_carbon_share_elec', 'fossil_share_elec']]

st.markdown('### Distribución global')

year = st.slider(label="Año a visualizar:", min_value=1960, max_value=2023, value=2023, step=1)

energy = st.selectbox(
    'Tipo de energía a comparar.',
    ['low_carbon_share_elec', 'fossil_share_elec'],
    index=0,
    placeholder='Seleccione un elemento'
)

if energy=='low_carbon_share_elec':
    color = px.colors.sequential.Viridis
else:
    color = px.colors.sequential.Inferno_r

fig = px.choropleth(df[df['year']==year], locations="iso_code",
                    color=energy, # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=color)

fig.update_geos(projection_type="natural earth")
#fig.update_geos(projection_type="orthographic")
fig.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)