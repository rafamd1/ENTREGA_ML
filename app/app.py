import streamlit as st
import joblib
import pandas as pd

cd C:\Users\rafam\OneDrive\Documentos\GitHub\ENTREGA_FRAUDE\ENTREGA_ML

streamlit run app.py

model = joblib.load('best_model.pkl')

# Entrada de datos
st.write("Introduce los datos para la predicción:")

amt = st.number_input('Monto (amt)')
is_3x_above_mean = st.selectbox('¿Es 3 veces superior al promedio? (is_3x_above_mean)', [0, 1])
is_fraud_zip = st.selectbox('¿Es un código postal fraudulento? (is_fraud_zip)', [0, 1])
is_frequent_fraudster = st.selectbox('¿Es un defraudador frecuente? (is_frequent_fraudster)', [0, 1])

# Realizar predicción
if st.button('Predecir'):
    nuevo_registro = pd.DataFrame({
        'amt': [amt],
        'is_3x_above_mean': [is_3x_above_mean],
        'is_fraud_zip': [is_fraud_zip],
        'is_frequent_fraudster': [is_frequent_fraudster],
    })
    prediction = model.predict(nuevo_registro)
    st.write(f'La predicción del modelo es: {prediction[0]}')

streamlit run app.py


st.title('Aplicación de Predicción de Fraude')
