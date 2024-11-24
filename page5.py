import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('owid-energy-data.csv').fillna(0)
df=df[['country', 'year', 'iso_code', 'low_carbon_share_elec', 'fossil_share_elec']].sort_values(by=['year'])

st.markdown('### Distribución global')

#year = st.slider(
#    label="Año a visualizar:",
#    min_value=df['year'].min(),
#    max_value=df['year'].max(),
#    value=df['year'].max(),
#    step=1
#)

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

fig = px.choropleth(
    df,
    locations="iso_code",
    color=energy,
    hover_name="country",
    animation_frame="year",
    color_continuous_scale=color
)

fig.update_geos(projection_type="natural earth")
#fig.update_geos(projection_type="orthographic")
fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)
