import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Painel Asiático ZETA")

@st.cache_data(ttl=60)
def obter_sinais():
    # --- EXEMPLO de sinais simulados --------------------
    agora = datetime.now().strftime("%H:%M:%S")
    dados = [
        {"Par": "AUD/CAD", "Direção": "CALL", "Confiança": 97, "Hora": agora},
        {"Par": "EUR/JPY", "Direção": "PUT",  "Confiança": 98, "Hora": agora},
    ]
    return pd.DataFrame(dados)

df = obter_sinais()
st.title("Painel Asiático – Sinais em tempo real")
st.dataframe(df, use_container_width=True)
