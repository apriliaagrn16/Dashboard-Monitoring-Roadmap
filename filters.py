import streamlit as st
import pandas as pd

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.title("🔍 Filter Data")

    date_range = st.sidebar.date_input(
        "Rentang Tanggal",
        [df['Date'].min().date(), df['Date'].max().date()]
    )

    tujuan = st.sidebar.multiselect(
        "Tujuan",
        options=df['Tujuan'].dropna().unique(),
        default=df['Tujuan'].dropna().unique()
    )

    gender = st.sidebar.multiselect(
        "Jenis Kelamin",
        options=df['Jenis Kelamin'].dropna().unique(),
        default=df['Jenis Kelamin'].dropna().unique()
    )

    sumber = st.sidebar.multiselect(
        "Tau Free Roadmap Dari",
        options=df['Kamu tau free roadmap & training ini darimana?'].dropna().unique(),
        default=df['Kamu tau free roadmap & training ini darimana?'].dropna().unique()
    )

    monetisasi = st.sidebar.multiselect(
        "Sudah Menghasilkan Uang?",
        options=df['Apakah kamu sudah menghasilkan uang dari sosmed?'].dropna().unique(),
        default=df['Apakah kamu sudah menghasilkan uang dari sosmed?'].dropna().unique()
    )

    filtered_df = df[
        (df['Date'].dt.date >= date_range[0]) &
        (df['Date'].dt.date <= date_range[1]) &
        (df['Tujuan'].isin(tujuan)) &
        (df['Jenis Kelamin'].isin(gender)) &
        (df['Kamu tau free roadmap & training ini darimana?'].isin(sumber)) &
        (df['Apakah kamu sudah menghasilkan uang dari sosmed?'].isin(monetisasi))
    ]

    return filtered_df
