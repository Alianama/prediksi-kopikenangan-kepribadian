# Ngopi Yuk! - Streamlit App Prediksi Jenis Kopi Berdasarkan Kepribadian (Gamified & Enhanced)

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
from PIL import Image

# ---------------------------
# 1. Load Dataset dari CSV
# ---------------------------
data = pd.read_csv("menu_kopi_kenangan.csv")

# Preprocessing: Label encoding untuk semua kolom kecuali harga
encoders = {}
data_encoded = data.copy()
for column in data.columns:
    if data[column].dtype == 'object' and column != 'Nama Menu' and column != 'Komposisi':
        encoders[column] = LabelEncoder()
        data_encoded[column] = encoders[column].fit_transform(data[column])

# Fitur yang digunakan untuk prediksi (tanpa Nama Menu, Komposisi, Harga)
X = data_encoded.drop(["Nama Menu", "Komposisi", "Harga"], axis=1)
y = data_encoded["Nama Menu"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Untuk mapping hasil prediksi
label_mapping = dict(zip(data_encoded["Nama Menu"], data["Nama Menu"]))

# ---------------------------
# 3. Streamlit UI
# ---------------------------
st.set_page_config(page_title="Ngopi Yuk!", page_icon="☕", layout="centered")

# Custom CSS ala Kopi Kenangan
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Pacifico&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background: #fff;
    }
    .kopi-title {
        font-family: 'Pacifico', cursive;
        color: #111;
        font-size: 2.7rem;
        margin-bottom: 0.2em;
        margin-top: 0.2em;
        letter-spacing: 1px;
        text-align: center;
    }
    .stButton>button {
        background-color: #b71c1c !important;
        color: #fff !important;
        border-radius: 30px !important;
        font-weight: bold;
        font-family: 'Montserrat', sans-serif;
        border: none;
        padding: 0.6em 2em;
    }
    .stButton>button:hover {
        background-color: #d32f2f !important;
        color: #fff !important;
    }
    .stRadio>div>label, .stSelectbox>div>div, .stMultiSelect>div>div {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
    }
    .footer {
        text-align: center;
        color: #b71c1c;
        font-size: 1rem;
        margin-top: 2em;
        font-family: 'Montserrat', sans-serif;
        opacity: 0.8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("kopi_kenangan_logo.png")
st.markdown('<div class="kopi-title">Ngopi Yuk!<br><span style="font-size:1.2rem;font-family:Montserrat,sans-serif;font-weight:400;">Prediksi Kopi Kenangan Favoritmu</span></div>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("---")
st.markdown("#### 🧠 Kuis Kepribadian Kopimu untuk Rekomendasi Menu Kopi Kenangan")
st.markdown("Isi semua pertanyaan di bawah dan temukan menu yang cocok!")

with st.form("quiz"):
    col1, col2 = st.columns(2)
    with col1:
        tipe_kepribadian = st.selectbox("Tipe Kepribadian", ["Santai", "Sibuk dan Produktif", "Petualang", "Pemikir", "Romantis", "Ambisius", "Humoris", "Introvert", "Ekstrovert", "Perfeksionis"])
        manis = st.slider("Seberapa suka rasa manis?", 1, 5, 3, format="%d", help="1=Tidak Suka, 5=Sangat Suka")
        malam = st.slider("Seberapa aktif di malam hari?", 1, 5, 3, format="%d", help="1=Jarang, 5=Selalu")
    with col2:
        nongkrong = st.slider("Seberapa suka nongkrong di cafe?", 1, 5, 3, format="%d", help="1=Tidak Suka, 5=Sangat Suka")
        kreatif = st.slider("Seberapa kreatif kamu?", 1, 5, 3, format="%d", help="1=Tidak Kreatif, 5=Sangat Kreatif")
    submitted = st.form_submit_button("🎯 Rekomendasikan Menu!")

def mapping_kepribadian_to_menu(tipe_kepribadian, manis, malam, nongkrong, kreatif):
    # Mapping slider ke Ya/Tidak
    def skala_to_ya_tidak(val):
        return "Ya" if val > 3 else "Tidak"
    tipe = "Kopi"
    if kreatif > 3:
        tipe = "Oatside"
    elif tipe_kepribadian in ["Santai", "Romantis"]:
        tipe = "Non-Kopi"
    elif tipe_kepribadian in ["Ambisius", "Sibuk dan Produktif"]:
        tipe = "Kopi"
    elif tipe_kepribadian in ["Petualang"]:
        tipe = "Freezy"
    elif tipe_kepribadian in ["Perfeksionis"]:
        tipe = "Kopi"
    elif tipe_kepribadian in ["Humoris"]:
        tipe = "Camilan"
    elif tipe_kepribadian in ["Introvert"]:
        tipe = "Non-Kopi"
    elif tipe_kepribadian in ["Ekstrovert"]:
        tipe = "Kopi"
    rasa_manis = skala_to_ya_tidak(manis)
    ada_susu = "Ya" if tipe != "Kopi" or kreatif > 3 else "Tidak"
    ada_kopi = "Ya" if tipe in ["Kopi", "Oatside", "Freezy"] else "Tidak"
    ada_boba = "Ya" if nongkrong > 3 and tipe in ["Oatside", "Non-Kopi"] else "Tidak"
    favorit = "Ya" if tipe_kepribadian in ["Santai", "Ambisius", "Romantis"] else "Tidak"
    return {
        "Tipe": tipe,
        "Rasa Manis": rasa_manis,
        "Ada Susu": ada_susu,
        "Ada Kopi": ada_kopi,
        "Ada Boba": ada_boba,
        "Favorit": favorit
    }

if submitted:
    fitur_menu = mapping_kepribadian_to_menu(tipe_kepribadian, manis, malam, nongkrong, kreatif)
    input_df = pd.DataFrame([fitur_menu])
    input_encoded = input_df.copy()
    for column in input_df.columns:
        if column in encoders:
            input_encoded[column] = encoders[column].transform(input_df[column])

    # Tidak ada filter dataset berdasarkan ekonomi, gunakan seluruh data
    # Prediksi pada seluruh data
    if not data_encoded.empty:
        X_all = data_encoded.drop(["Nama Menu", "Komposisi", "Harga"], axis=1)
        model_all = KNeighborsClassifier(n_neighbors=3)
        model_all.fit(X_all, data_encoded["Nama Menu"])
        pred = model_all.predict(input_encoded)[0]
        result = label_mapping[pred]
        harga = data.loc[data["Nama Menu"] == result, "Harga"].values[0]
        komposisi = data.loc[data["Nama Menu"] == result, "Komposisi"].values[0]
        st.success(f"🎉 Rekomendasi menu untukmu: **{result}**\n\nHarga: Rp{harga:,}\nKomposisi: {komposisi}")
        st.balloons()
    else:
        st.warning("Tidak ada menu yang tersedia!")

    st.markdown("---")
    st.markdown("### 📊 Statistik Menu")
    fig = px.pie(data, names="Tipe", title="Distribusi Tipe Menu Kopi Kenangan")
    st.plotly_chart(fig)

    st.markdown("Dataset menu diambil dari menu_kopi_kenangan.csv!")
    st.markdown("---")
    st.info("✨ Coba kepribadian lain untuk rekomendasi berbeda!")

st.markdown('<div class="footer">©2025 Ali Purnama | <b>@Universitas Pelita Bangsa</b></div>', unsafe_allow_html=True)
