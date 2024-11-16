import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df = pd.read_csv('owid-energy-data.csv')
df_countries = df['country'].drop_duplicates()
st.markdown('### Energías tradicionales vs renovables')

countries = st.multiselect(
    'Seleccione los paises o agrupaciones a comparar.',
    df_countries,
    [],
    placeholder='Seleccione 2 o más elementos'
)

fig = go.Figure()
for country in countries:
    fig.add_trace(
        go.Scatter(x=list(df[df['country']==country].year), y=list(df[df['country']==country].fossil_electricity), name=f'Energías no renovables de {country}')
    )
    fig.add_trace(
        go.Scatter(x=list(df[df['country']==country].year), y=list(df[df['country']==country].renewables_electricity), name=f'Energías renovables de {country}')
    )

fig.update_layout(
    title_text="Energías tradicionales vs renovables"
)

fig.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

st.plotly_chart(fig)
