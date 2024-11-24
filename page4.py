import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-energy-data.csv').fillna(0)
df = df[['country', 'year', 'low_carbon_share_elec', 'fossil_share_elec']]

st.markdown('### Energías renovables entre paises')

year = st.slider(
    label="Año a visualizar:",
    min_value=df['year'].min(),
    max_value=df['year'].max(),
    value=df['year'].max(),
    step=1
)

fig = px.histogram(df[df['year']==year], x='low_carbon_share_elec', nbins=20)

st.plotly_chart(fig)