import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo treinado
model = joblib.load('modelo.pkl')

st.set_page_config(page_title="Detector de Fraudes 💳", layout="centered")
st.title("💳 Detector de Fraudes com IA")
st.markdown("Insira os dados simulados da transação abaixo para verificar possíveis fraudes.")

# Entradas simuladas
amount = st.number_input("Valor da Transação (Amount)", min_value=0.0, value=100.0)
v1 = st.slider("V1", -30.0, 30.0, value=0.0)
v2 = st.slider("V2", -30.0, 30.0, value=0.0)

# Variáveis restantes como 0 para simplificação
input_data = pd.DataFrame([[amount, v1, v2] + [0]*27], columns=model.feature_names_in_)

# Previsão
if st.button("Detectar"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("🚨 FRAUDE DETECTADA!")
    else:
        st.success("✅ Transação legítima.")
