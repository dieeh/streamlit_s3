import streamlit as st
import pandas as pd

df = pd.read_csv('owid-energy-data.csv').fillna(0)

st.markdown('### Energías renovables entre paises')