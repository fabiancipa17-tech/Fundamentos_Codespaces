import streamlit as st

st.title('¡Hola, Codespaces y Copilot!')
st.write('Esta es una app de ejemplo usando Streamlit en un entorno virtual.')

st.header('Interacción')
nombre = st.text_input('¿Cuál es tu nombre?')
if nombre:
    st.success(f'¡Bienvenido, {nombre}!')
