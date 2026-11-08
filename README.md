# Análisis de generación eléctrica y fuentes de energía

Dashboard interactivo desarrollado con **Python**, **Streamlit**, **Pandas** y **Plotly** para explorar la generación eléctrica y la participación de distintas fuentes energéticas a nivel mundial.

La aplicación permite comparar países y agrupaciones, analizar la evolución histórica de la generación eléctrica y explorar la distribución geográfica de las fuentes de energía.

## Funcionalidades

La aplicación está organizada en cinco vistas:

1. **Energías tradicionales vs. renovables:** compara la generación eléctrica de fuentes fósiles y renovables a lo largo del tiempo para uno o más países.
2. **Tipos de energías renovables:** permite explorar la evolución de la generación solar, eólica, hídrica y por biocombustibles.
3. **Distribución de energía:** muestra la composición de la generación eléctrica de un país o agrupación en un año determinado.
4. **Comparación entre países:** presenta la distribución de la participación de electricidad de bajas emisiones de carbono para un año seleccionado.
5. **Distribución global:** visualiza en un mapa mundial animado la participación de fuentes de bajas emisiones de carbono o combustibles fósiles por país y año.

Los gráficos incluyen controles interactivos para seleccionar países, años y variables, además de explorar valores y tendencias.

## Tecnologías

- **Python** — lenguaje de programación.
- **Streamlit** — interfaz web y navegación multipágina.
- **Pandas** — lectura, selección y transformación de datos.
- **Plotly** — gráficos de líneas, dona, histogramas y mapas coropléticos.

## Estructura del proyecto

```text
streamlit_s3/
├── main.py                    # Configuración y navegación de la aplicación
├── page1.py                   # Fuentes tradicionales vs. renovables
├── page2.py                   # Comparación de fuentes renovables
├── page3.py                   # Composición de la generación eléctrica
├── page4.py                   # Distribución de electricidad de bajas emisiones
├── page5.py                   # Mapa mundial por país y año
├── owid-energy-data.csv       # Dataset de generación eléctrica
├── owid-energy-codebook.csv   # Descripción de variables del dataset
├── dashboard.png              # Imagen utilizada en la interfaz
├── requirements.txt           # Dependencias de Python
```

## Ejecución local

Se requiere Python y `pip`.

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/dieeh/streamlit_s3.git
   cd streamlit_s3
   ```

2. Crear y activar un entorno virtual (opcional, recomendado):

   ```bash
   python -m venv .venv
   ```

   En Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   En Linux o macOS:

   ```bash
   source .venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Iniciar la aplicación:

   ```bash
   streamlit run main.py
   ```

Streamlit mostrará la dirección local para abrir el dashboard en el navegador.

## Datos

El proyecto utiliza el conjunto de datos de energía de **Our World in Data**, incluido en el repositorio como `owid-energy-data.csv`. El archivo `owid-energy-codebook.csv` contiene la descripción de las variables disponibles.

- Fuente: [Our World in Data — Energy](https://ourworldindata.org/energy)
- Los archivos incluidos corresponden a una copia del dataset y no se actualizan automáticamente.

**Nota metodológica:** los scripts actuales reemplazan valores faltantes por cero al cargar el dataset. Por lo tanto, los resultados deben interpretarse considerando que un dato ausente puede no representar necesariamente una generación igual a cero.

## Alcance

Proyecto académico de análisis exploratorio y visualización de datos. Las visualizaciones permiten explorar patrones y comparar indicadores, pero no constituyen por sí mismas un análisis causal ni una evaluación de políticas energéticas.
