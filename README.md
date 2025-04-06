# 📊 Proyecto Índice GINI - Python + C + ASM

Este proyecto tiene como objetivo diseñar e implementar una interfaz multicapas para mostrar el índice GINI de países, utilizando datos de la API del Banco Mundial.

## 🧠 Tecnologías utilizadas

- Python 🐍 (API REST y visualización)
- C 💻 (capa intermedia y lógica)
- Ensamblador (futuro, operaciones de bajo nivel)
- Git & GitHub 🌐
- Makefile 🛠️
- Testing y documentación 📚

## 📂 Estructura esperada



```
├── c/ # Código fuente en C y ensamblador 
├── python/ # Scripts en Python 
├── tests/ # Casos de prueba 
├── docs/ # Diagramas y documentación técnica 
├── Makefile # Automatización de compilación 
└── README.md # Descripción general del proyecto 
``` 
## 📌 Objetivo de la primera etapa

Integrar Python con C usando `ctypes`. Se realizará:
- Consulta a la API del Banco Mundial
- Extracción del índice GINI de Argentina
- Envío del valor como `float` a C
- C lo convierte a entero, suma 1 y lo devuelve
- Python muestra el resultado

## 🔄 Próximas etapas

- Implementación de rutinas en ensamblador
- Pruebas automáticas y profiling
- Mejoras en visualización y exportación de datos

## 🔧 Cómo colaborar

Se trabajará en ramas:
- `main`: rama estable
- `dev`: rama de integración
- `feature/*`: desarrollo de nuevas funcionalidades
---


