import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

#fig1 = px.choropleth(df, )
fig = go.Figure(go.Scattergeo())
fig.update_geos(
    projection_type="natural earth",
    showcountries=True, 
    countrycolor="RebeccaPurple"
    )
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig)