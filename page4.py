import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('owid-energy-data.csv').fillna(0) # se lee el dataframe y se reemplazan los NaN con ceros
df = df[['country', 'year', 'low_carbon_share_elec', 'fossil_share_elec']]

st.markdown('### Energías renovables entre paises')

year = st.slider( # st.slider permite elegir un valor numerico entre 2 topes
    label="Año a visualizar:",
    min_value=df['year'].min(),
    max_value=df['year'].max(),
    value=df['year'].max(),
    step=1
)

fig = px.histogram(df[df['year']==year], x='low_carbon_share_elec', marginal="rug") 
# se grafica el histograma de frecuencia de porcentajes de uso de energias renovables

fig.update_layout(
    title_text='Porcentaje de energías renovables a nivel mundial', # title of plot
    xaxis_title_text='Porcentaje', # xaxis label
    yaxis_title_text='Cantidad', # yaxis label
    bargap=0.2 # gap between bars of adjacent location coordinates
    #bargroupgap=0.1 # gap between bars of the same location coordinates
)

st.plotly_chart(fig)
