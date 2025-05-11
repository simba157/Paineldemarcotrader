import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="Painel Asiático – Sinais em tempo real", layout="wide")
st.title("Painel Asiático ZETA")

@st.cache_data(ttl=60)
def obter_sinais():
    # EXEMPLO: sinais simulados
    agora = datetime.now().strftime("%H:%M")
    dados = [
        {"Par":"AUD/CAD","Direção":"CALL","Confiança":97,"Hora":agora},
        {"Par":"EUR/JPY","Direção":"PUT","Confiança":99,"Hora":agora},
    ]
    return pd.DataFrame(dados)

df = obter_sinais()
st.dataframe(df, use_container_width=True)
