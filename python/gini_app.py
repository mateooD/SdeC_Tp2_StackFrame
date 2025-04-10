import streamlit as st
import requests
import pandas as pd
import ctypes
import os

st.set_page_config(page_title="Índice de Gini - Banco Mundial", layout="centered")
st.title("📊 Índice de Gini por País")
st.markdown("Fuente de datos: [Banco Mundial](https://data.worldbank.org/indicator/SI.POV.GINI)")

# Cargar librería C
lib_path = os.path.join(os.path.dirname(__file__), '..', 'c', 'libgini.so')
gini_lib = ctypes.CDLL(lib_path)
gini_lib.convertir_y_sumar.argtypes = [ctypes.c_float]
gini_lib.convertir_y_sumar.restype = ctypes.c_int

# Obtener lista de países desde la API del Banco Mundial
@st.cache_data(show_spinner="Cargando países disponibles...")
def get_paises_disponibles():
    url = "https://api.worldbank.org/v2/country?format=json&per_page=300"
    response = requests.get(url)
    try:
        data = response.json()[1]
        paises = {
            item["name"]: item["id"]
            for item in data
            if item["region"]["id"] != "NA" and item["incomeLevel"]["id"] != "NA"
        }
        return dict(sorted(paises.items()))  # Orden alfabético
    except:
        return {}

PAISES = get_paises_disponibles()

# Entrada de usuario
col1, col2 = st.columns(2)

with col1:
    pais_seleccionado = st.selectbox("Selecciona un país", list(PAISES.keys()))
    country_code = PAISES[pais_seleccionado]

with col2:
    year_range = st.slider("Selecciona el rango de años", 1990, 2022, (2011, 2020))

# Obtener y procesar datos
@st.cache_data(show_spinner=True)
def get_gini_data_processed(country, start_year, end_year):
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
        return pd.DataFrame()

    rows = []
    for entry in data:
        year = entry.get("date")
        value = entry.get("value")
        if year and value is not None:
            try:
                processed_value = gini_lib.convertir_y_sumar(ctypes.c_float(value))
                rows.append({
                    "Año": int(year),
                    "Índice de Gini (original)": round(value, 2),
                    "Índice de Gini (procesado)": processed_value
                })
            except Exception as e:
                print(f"Error procesando el valor {value} del año {year}: {e}")

    df = pd.DataFrame(rows)
    if not df.empty:
        return df.sort_values("Año")
    return df

# Mostrar resultados
df = get_gini_data_processed(country_code, year_range[0], year_range[1])

if not df.empty:
    st.subheader(f"📈 Evolución del Índice de Gini en {pais_seleccionado}")
    st.line_chart(df.rename(columns={"Año": "index"}).set_index("index")["Índice de Gini (procesado)"])

    with st.expander("📄 Ver tabla de datos"):
        st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar CSV",
        data=csv,
        file_name=f"gini_{country_code}_{year_range[0]}_{year_range[1]}.csv",
        mime="text/csv"
    )
else:
    st.warning("No se encontraron datos para ese país o período.")
