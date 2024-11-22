import streamlit as st

st.set_page_config(layout="wide")
st.logo("temp1.png",size='large', icon_image="temp2.png")
pg = st.navigation({
    'Comparaciones':[
        st.Page("page1.py",title='E. Tradicionales vs Renovables', icon=':material/home:'),
        st.Page("page2.py",title='Tipos de energías renovables', icon=':material/star:'),
        st.Page("page3.py",title='Distribución de energía', icon=':material/bolt:'),
        st.Page("page4.py",title='E. renovables entre paises', icon=':material/done_all:'),
        st.Page("page5.py",title='Distribución Global', icon=':material/public:'),
        ]
    }
)
pg.run()
