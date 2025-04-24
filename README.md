# 📊 Proyecto Índice GINI - Python + C + ASM

Este proyecto tiene como objetivo diseñar e implementar una interfaz multicapas para mostrar el índice GINI de países, utilizando datos de la API del Banco Mundial.

## 🧠 Tecnologías utilizadas

- Python 🐍 (API REST y visualización)
- C 💻 (capa intermedia y lógica)
- Assembly 
- ESP32 + PlatformIO
- Streamlit
- API del Banco Mundial (World Bank Open Data)
- Git & GitHub 🌐
- Makefile 🛠️


## 📂 Estructura

```
├── c/ # Código fuente en C y ensamblador 
├── python/ # Scripts en Python 
├── esp32_webserver/ # Proyecto PlatformIO con ESP32 como servidor embebido
├── docs/ # Diagramas y documentación técnica 
├── Makefile # Automatización de compilación 
└── README.md # Descripción general del proyecto 
``` 

## 🚀 ¿Cómo correr el proyecto?

### 1. Streamlit App

```bash
cd python
streamlit run main.py
```
Asegurate de configurar correctamente tu red WiFi en el archivo main.cpp.
Podras visualizar la app en un host local o en una IP brindada.

### 2. Proyecto ESP32 (PlatformIO)

```bash
cd esp32_webserver
pio run -t upload && pio run -t monitor
```
En el monitor serial corroboras el funcionamiento, como asi tambien la IP de el servidor embebido.
Para la visualizacion de los datos añadir el endpoint /ver

### 3. Comunicación App ↔️ ESP32

En la interfaz Streamlit, se puede ingresar la IP local de la ESP32 para enviarle datos procesados en tiempo real y mostrarlos en la web embebida.

### Ejemplos de uso 

- Seleccionás un país y un rango de años.

- La app muestra la evolución del Índice de Gini (original y procesado).

- Se puede probar la conexión con la ESP32 y enviar datos.
