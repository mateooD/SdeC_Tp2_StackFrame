import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Índice de Gini - Banco Mundial", layout="centered")

st.title("📊 Índice de Gini por País")
st.markdown("Fuente de datos: [Banco Mundial](https://data.worldbank.org/indicator/SI.POV.GINI)")

# Entrada de usuario
col1, col2 = st.columns(2)

with col1:
    country_code = st.text_input("Código del país (ISO-2)", "AR").upper()

with col2:
    year_range = st.slider("Selecciona el rango de años", 1990, 2022, (2011, 2020))

# Función para obtener datos desde la API
@st.cache_data(show_spinner=True)
def get_gini_data(country, start_year, end_year):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/SI.POV.GINI"
    params = {
        "format": "json",
        "date": f"{start_year}:{end_year}",
        "per_page": 100
    }
    response = requests.get(url, params=params)
    
    try:
        data = response.json()[1]
    except:
        return pd.DataFrame()  # Si no hay datos

    df = pd.DataFrame(data)
    df = df[["date", "value"]].dropna()
    df.columns = ["Año", "Índice de Gini"]
    df["Año"] = df["Año"].astype(int)
    return df.sort_values("Año")

# Obtener datos
df = get_gini_data(country_code, year_range[0], year_range[1])

# Mostrar resultados
if not df.empty:
    st.subheader(f"📈 Evolución del Índice de Gini en {country_code}")
    st.line_chart(df.rename(columns={"Año": "index"}).set_index("index"))

    with st.expander("📄 Ver tabla de datos"):
        st.dataframe(df, use_container_width=True)

    # Opción para descargar CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar CSV",
        data=csv,
        file_name=f"gini_{country_code}_{year_range[0]}_{year_range[1]}.csv",
        mime="text/csv"
    )
else:
    st.warning("No se encontraron datos para ese país o período.")
