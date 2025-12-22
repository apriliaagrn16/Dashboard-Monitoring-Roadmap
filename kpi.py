import streamlit as st
import pandas as pd

def show_kpi(df: pd.DataFrame):
    col1, col2, col3, col4, col5, = st.columns(5)

    # ===== TOTAL USER =====
    col1.metric("👥 Total User", len(df))

    # ===== RATA-RATA UMUR =====
    df['umur_fix'] = pd.to_numeric(df['umur'], errors='coerce')
    df_umur_valid = df[(df['umur_fix'] >= 0) & (df['umur_fix'] <= 100)]
    avg_age = df_umur_valid['umur_fix'].mean()
    col2.metric("📊 Rata-rata Umur", f"{avg_age:.1f} tahun" if not pd.isna(avg_age) else "-")

    # ===== USER BULAN TERAKHIR =====
    if 'month' in df.columns:
        col3.metric(
            "📅 User Bulan Terakhir",
            df[df['month'] == df['month'].max()].shape[0]
        )
    else:
        col3.metric("📅 User Bulan Terakhir", "-")

    # ===== GENDER =====
    if 'Jenis Kelamin' in df.columns:
        laki = df[df['Jenis Kelamin']
                  .str.lower()
                  .str.contains('laki|pria', na=False)].shape[0]

        perempuan = df[df['Jenis Kelamin']
                       .str.lower()
                       .str.contains('perempuan|wanita', na=False)].shape[0]

        col4.metric("👨 Laki-laki", laki)
        col5.metric("👩 Perempuan", perempuan)
    else:
        col4.metric("👨 Laki-laki", "-")
        col5.metric("👩 Perempuan", "-")
