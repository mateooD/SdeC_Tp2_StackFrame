# Changelog

Todas las versiones importantes de este proyecto serán documentadas aquí.

## [v0.1] - 2025-04-06
### Agregado
- Integración inicial entre Python y C.
- Uso de `ctypes` para invocar funciones C desde Python.
- Procesamiento del valor GINI: conversión float a int, suma +1.
- Recuperación de datos desde la API del Banco Mundial (`https://api.worldbank.org/...`).

### Cambios
- Se creó `Makefile` para compilar la librería compartida `libgini.so`.
- Organización inicial del proyecto en carpetas `/c`, `/python`, `/tests`, `/docs`.

---

> Próximas versiones incluirán la integración con ensamblador y pruebas unitarias.