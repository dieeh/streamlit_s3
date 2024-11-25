import streamlit as st

st.set_page_config(layout="wide") # st.set_page_config cambia la distribución de la pagina, y layout='wide' hace que ocupe el ancho total
st.logo("dashboard.png",size='large', icon_image="dashboard.png") # st.logo permite añadir logos al sidebar y pagina
pg = st.navigation({
        'Comparaciones':[
            st.Page("page1.py",title='E. Tradicionales vs Renovables', icon=':material/stacked_line_chart:'),
            st.Page("page2.py",title='Tipos de energías renovables', icon=':material/ssid_chart:'),
            st.Page("page3.py",title='Distribución de energía', icon=':material/pie_chart:'),
            st.Page("page4.py",title='E. renovables entre paises', icon=':material/bar_chart:'),
            st.Page("page5.py",title='Distribución Global', icon=':material/public:'),
        ]
    }
)
pg.run()
