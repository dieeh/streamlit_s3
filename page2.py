import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('owid-energy-data.csv').fillna(0)
df_countries = df['country'].drop_duplicates()
st.markdown('### Tipos de energías renovables')

countries = st.selectbox(
    'País o agrupación a comparar.',
    df_countries,
    index=None,
    placeholder='Seleccione un elemento'
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=list(df[df['country']==countries].year),
        y=list(df[df['country']==countries].solar_electricity),
        name='Energía Solar',
        yaxis="y"
        )
)
fig.add_trace(
    go.Scatter(
        x=list(df[df['country']==countries].year),
        y=list(df[df['country']==countries].wind_electricity),
        name='Energía Eólica',
        yaxis="y"
        )
)
fig.add_trace(
    go.Scatter(
        x=list(df[df['country']==countries].year),
        y=list(df[df['country']==countries].hydro_electricity),
        name='Energía Hídrica',
        yaxis="y"
        )
)
fig.add_trace(
    go.Scatter(
        x=list(df[df['country']==countries].year),
        y=list(df[df['country']==countries].biofuel_electricity),
        name='Energía por biocombustibles',
        yaxis="y"
        )
)

fig.update_layout(
    title_text="Tipos de energías renovables",
    xaxis=dict(
        range=["1950", "2024"],
        rangeslider=dict(
            visible=True
        ),
        type="linear"
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

fig.update_traces(mode="lines", hovertemplate=None, hoverlabel = dict(namelength = -1))
fig.update_layout(hovermode="x unified")

st.plotly_chart(fig)
