import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="Painel Asiático ZETA")

# --- URL da sua API no Render ---
API_URL = "https://api-sniper-asiatico.onrender.com/sinais"

@st.cache_data(ttl=20)        # cache de 20 s
def obter_sinais():
    """
    Busca sinais reais na API.
    Retorna um DataFrame vazio se der erro.
    """
    try:
        resp = requests.get(API_URL, timeout=10)
        resp.raise_for_status()
        dados = resp.json()              # a API devolve lista de dicionários
        return pd.DataFrame(dados)
    except Exception as e:
        st.error(f"Erro ao acessar API: {e}")
        return pd.DataFrame()

# --- Interface ---
df = obter_sinais()
st.title("Painel Asiático – Sinais em tempo real")
st.dataframe(df, use_container_width=True)
