import streamlit as st
import pandas as pd
import numpy as np

st.title('Ejemplo: Gráfica de datos aleatorios')

st.write('Este ejemplo muestra cómo graficar datos generados aleatoriamente usando Streamlit.')

data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)

st.write('Puedes recargar la app para ver nuevos datos aleatorios.')
