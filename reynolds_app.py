import streamlit as st

st.title('Cálculo del Número de Reynolds')

st.write('Esta app calcula el número de Reynolds y determina el tipo de flujo.')

# Entradas del usuario
densidad = st.number_input('Densidad del fluido (kg/m³)', min_value=0.0, value=1000.0)
velocidad = st.number_input('Velocidad del fluido (m/s)', min_value=0.0, value=1.0)
diametro = st.number_input('Diámetro del tubo (m)', min_value=0.0, value=0.1)
viscosidad = st.number_input('Viscosidad dinámica (Pa·s)', min_value=0.000001, value=0.001)

if st.button('Calcular'):
    reynolds = (densidad * velocidad * diametro) / viscosidad
    st.write(f'**Número de Reynolds:** {reynolds:.2f}')

    if reynolds < 2000:
        st.success('Flujo laminar')
    elif 2000 <= reynolds <= 4000:
        st.warning('Flujo de transición')
    else:
        st.info('Flujo turbulento')
