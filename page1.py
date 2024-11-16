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


