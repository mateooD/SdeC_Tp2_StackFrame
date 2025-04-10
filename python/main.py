import ctypes
import os
import requests
#from msl.loadlib import LoadLibrary

# Cargar la librería compartida desde el path correcto
lib_path = os.path.join(os.path.dirname(__file__), '..', 'c', 'libgini.so')
gini_lib = ctypes.CDLL(lib_path)
#gini_lib = LoadLibrary(lib_path)

# Configurar los tipos de la función
gini_lib.convertir_y_sumar.argtypes = [ctypes.c_float]
gini_lib.convertir_y_sumar.restype = ctypes.c_int

#  Obtener el valor GINI desde la API
url = "https://api.worldbank.org/v2/en/country/AR/indicator/SI.POV.GINI?format=json&date=2020&per_page=1"
response = requests.get(url)
data = response.json()

try:
    valor = data[1][0]['value']
    if valor is None:
        raise ValueError("No hay datos disponibles.")
except (IndexError, KeyError, ValueError) as e:
    print("Error al obtener el valor del índice GINI:", e)
    exit(1)

#Llamar a la función en C
resultado = gini_lib.convertir_y_sumar(valor)

#Mostrar resultados
print(f"Valor GINI obtenido desde la API: {valor}")
print(f"Resultado procesado en C: {resultado}")