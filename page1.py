import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('owid-energy-data.csv').fillna(0) # se lee el dataframe y se reemplazan los NaN con ceros
df_countries = df['country'].drop_duplicates() # se copia la columna de los nombres de paises/agrupaciones y se eliminan los duplicados
st.markdown('### Energías tradicionales vs renovables') # st.markdown permite escribir texto

countries = st.multiselect( # st.multiselect permite seleccionar varios elementos de una lista
    'Paises o agrupaciones a comparar.',
    df_countries,
    ['Argentina','Chile'],
    placeholder='Seleccione 1 o más elementos'
)

fig = go.Figure() # go.Figure() crea la figura/grafico
for country in countries:
    fig.add_trace(
        go.Scatter(
            x=list(df[df['country']==country].year),
            y=list(df[df['country']==country].fossil_electricity),
            name=f'E. no renovables de {country}',
            yaxis="y"
            )
    )
    fig.add_trace(
        go.Scatter(
            x=list(df[df['country']==country].year),
            y=list(df[df['country']==country].renewables_electricity),
            name=f'E. renovables de {country}',
            yaxis="y"
            )
    )


fig.update_layout( # update_layout modifica los ejes y titulos
    title_text="Energías tradicionales vs renovables",
    xaxis=dict(
        range=["1950", "2024"],
        rangeslider=dict( # rangeslider es el que permite dar zoom en el grafico
            visible=True
        ),
        type="date"
    ),
    yaxis=dict(
        anchor="x",
        autorange=True,
        side="left",
        title=dict(
            text="TWh (Terawatt-hora)",
            font=dict(
                color="#607d8b"
            )
        ),
        type="linear",
        zeroline=True
    )
)

fig.update_traces(
    mode="lines",
    hovertemplate=None,
    hoverlabel = dict(namelength = -1)
)
fig.update_layout(hovermode="x unified")

st.plotly_chart(fig) #st.plotly_chart permite mostrar el grafico en streamlit
