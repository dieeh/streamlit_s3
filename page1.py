import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('owid-energy-data.csv')

st.dataframe(df.head())
