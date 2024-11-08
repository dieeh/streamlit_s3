import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pg = st.navigation({
    'Páginas':[
        st.Page("page1.py",title='Página 1', icon=':material/home:'),
    ]
}
)
pg.run()