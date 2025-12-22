import streamlit as st
from data_loader import load_data
from filters import apply_filters
from kpi import show_kpi
from charts import (
    chart_user_by_date,
    chart_tujuan,
    chart_sumber,
    chart_umur,
    chart_pertanyaan
)

st.set_page_config(
    page_title="Dashboard Monitoring User",
    layout="wide"
)

# ===== CONFIG =====
SHEET_ID = "128WokHgR0IRfdQr2jQjvG063kW9GI7NIx9HbuRVH5Nk"

# ===== LOAD DATA =====
df = load_data(SHEET_ID)

# ===== FILTER =====
filtered_df = apply_filters(df)

# ===== TITLE =====
st.title("📊 Dashboard Monitoring User")

# ===== KPI =====
show_kpi(filtered_df)

st.divider()

# ===== CHARTS =====
chart_user_by_date(filtered_df)
chart_tujuan(filtered_df)
chart_sumber(filtered_df)
chart_umur(filtered_df)
chart_pertanyaan(filtered_df)

st.divider()

# ===== TABLE =====
st.subheader("📋 Data User (Filtered)")
st.dataframe(filtered_df, use_container_width=True)
