import plotly.express as px
import streamlit as st
import pandas as pd

def chart_user_by_date(df: pd.DataFrame):
    data = (
        df.groupby(df['Date'].dt.date)
        .size()
        .reset_index(name='Jumlah User')
    )

    fig = px.line(
        data,
        x='Date',
        y='Jumlah User',
        markers=True,
        title="User Berdasarkan Tanggal"
    )
    st.plotly_chart(fig, use_container_width=True)

def chart_tujuan(df):
    data = (
        df['Tujuan']
        .value_counts()
        .reset_index(name='Jumlah User')
        .rename(columns={'index': 'Tujuan'})
    )

    fig = px.bar(
        data,
        x='Tujuan',
        y='Jumlah User',
        text='Jumlah User',
        color='Jumlah User',
        color_continuous_scale=[
            "#1e3a8a",  # biru gelap
            "#2563eb",  # biru utama
            "#38bdf8"   # biru terang
        ],
        title="🎯 Tujuan User"
    )

    fig.update_traces(
        textposition='outside'
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Jumlah User",
        bargap=0.25,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False  # hide legend gradasi
    )

    st.plotly_chart(fig, use_container_width=True)

def chart_sumber(df: pd.DataFrame):
    fig = px.pie(
        df,
        names='Kamu tau free roadmap & training ini darimana?',
        hole=0.4,
        title="User Tau Free Roadmap Dari Mana"
    )
    st.plotly_chart(fig, use_container_width=True)

def chart_umur(df: pd.DataFrame):
    df['umur_fix'] = pd.to_numeric(df['umur'], errors='coerce')

    # filter umur wajar
    df_umur_valid = df[
        (df['umur_fix'] >= 0) & (df['umur_fix'] <= 100)
    ]

    fig = px.histogram(
        df_umur_valid,
        x='umur_fix',
        nbins=15,
        title="Distribusi Umur"
    )

    st.plotly_chart(fig, use_container_width=True)


def chart_pertanyaan(df: pd.DataFrame):
    st.subheader("📝 Analisa Jawaban Pertanyaan")

    # 1. Clean the DataFrame columns first (removes accidental spaces)
    df.columns = df.columns.str.strip()

    # 2. Define the exact columns you want to visualize
    # Make sure these strings exist exactly in your CSV/Excel header
    options = [
        'Masalah TERBESAR kamu saat ini terkait konten/bisnis:',
        'Target utama kamu 3–6 bulan ke depan:',
        'Aktivitas',
        'Platform utama tempat kamu membangun audience/jualan:'
    ]
    
    # Check which options actually exist in the dataframe to prevent crashes
    available_options = [col for col in options if col in df.columns]

    if not available_options:
        st.error("None of the specified columns were found in the data.")
        return

    pertanyaan = st.selectbox("Pilih Pertanyaan", available_options)

    # 3. Process the data
    # We use 'index' because value_counts() puts the answers in the index
    counts = df[pertanyaan].value_counts().reset_index()
    
    # Rename columns safely
    counts.columns = ['Jawaban', 'Jumlah User']

    # 4. Create Plot
    fig = px.bar(
        counts,
        x='Jawaban',
        y='Jumlah User',
        title=f"Distribusi: {pertanyaan}",
        color='Jumlah User'
    )
    st.plotly_chart(fig, use_container_width=True)
