import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pg = st.navigation({
    'Comparaciones':[
        st.Page("page1.py",title='E. Tradicionales vs Renovables', icon=':material/home:'),
        st.Page("page2.py",title='Distribución de energías', icon=':material/star:')
    ]
}
)
pg.run()