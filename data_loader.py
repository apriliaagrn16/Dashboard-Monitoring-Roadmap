import pandas as pd
import streamlit as st
import requests
from io import StringIO

@st.cache_data(ttl=300, show_spinner="Mengambil data terbaru...")
def load_data(sheet_id: str) -> pd.DataFrame:
    url = f"https://docs.google.com/spreadsheets/d/128WokHgR0IRfdQr2jQjvG063kW9GI7NIx9HbuRVH5Nk/export?format=csv"
    response = requests.get(url, verify=False)  # <— fix SSL
    response.raise_for_status()

    df = pd.read_csv(StringIO(response.text))
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    df['umur'] = pd.to_numeric(df['umur'], errors='coerce')
    df.columns = (
    df.columns
    .str.strip()
    .str.replace("\n", " ")
)

    return df