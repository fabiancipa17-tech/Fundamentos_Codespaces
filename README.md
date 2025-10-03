
# Fundamentos_Codespaces

Este proyecto es un ejercicio introductorio al uso de GitHub Codespaces y GitHub Copilot, trabajando con Python y Streamlit en un entorno virtual.

## Estructura del proyecto

- Entorno virtual Python creado automáticamente en `.venv`.
- Dependencias gestionadas con `pip`.
- Ejemplo de aplicación con Streamlit.

## Requisitos previos

- Tener acceso a GitHub Codespaces.
- Python 3.12 o superior (el entorno se crea automáticamente en Codespaces).

## Instalación y uso

1. **Activar el entorno virtual:**
	```bash
	source .venv/bin/activate
	```

2. **Instalar dependencias:**
	(Ya instaladas automáticamente, pero puedes agregar más con)
	```bash
	pip install <paquete>
	```

3. **Ejecutar una app de Streamlit:**
	Crea un archivo, por ejemplo `app.py`, y ejecuta:
	```bash
	streamlit run app.py
	```

## Ejemplo básico de Streamlit

```python
import streamlit as st

st.title('¡Hola, Codespaces y Copilot!')
st.write('Esta es una app de ejemplo usando Streamlit en un entorno virtual.')
```

## Créditos

Autor: fabiancipa17-tech
