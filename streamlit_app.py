# app.py  ─── exemplo mínimo com “sinais”
import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="Painel Asiático", layout="wide")
st.title("Painel Asiático – Sinais em tempo real")

# --- Função que gera / busca seus sinais ---
@st.cache_data(ttl=60)  # atualiza a cada 60 s
def obter_sinais():
    # EXEMPLO 1: chamar uma API própria
    # resp = requests.get("https://meu-endpoint.com/sinais")
    # return pd.DataFrame(resp.json())

    # EXEMPLO 2: simular sinais locais (substitua pela sua lógica)
    agora = datetime.utcnow().strftime("%H:%M:%S")
    dados = [
        {"Par": "AUD/CAD", "Direção": "CALL", "Confiança": 97, "Hora": agora},
        {"Par": "EUR/JPY", "Direção": "PUT",  "Confiança": 99, "Hora": agora},
    ]
    return pd.DataFrame(dados)

df = obter_sinais()

st.subheader("⏰ Última atualização:")
st.write(datetime.utcnow().strftime("%d/%m/%Y  %H:%M:%S UTC"))

st.subheader("🔔 Sinais:")
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Confiança": st.column_config.ProgressColumn(
            min_value=0, max_value=100, format="%d%%"
        )
    },
)
st.caption("© ZETA Visão Total – sinais asiáticos")
