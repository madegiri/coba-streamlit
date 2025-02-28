import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

st.title("Kalkulator Luas Bangun Datar")
st.markdown("---")

# Sidebar menu
with st.sidebar:
    selected = option_menu("Dashboard", ["Persegi Panjang", "Persegi"], 
        icons=['square', 'grid'], menu_icon="cast", default_index=0)

# Perhitungan luas persegi panjang
if selected == "Persegi Panjang":
    st.header("Hitung Luas Persegi Panjang")

    panjang = st.number_input("Masukkan Nilai Panjang", 0)
    lebar = st.number_input("Masukkan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = panjang * lebar
        st.success(f"Luas Persegi Panjang = {luas}")

# Perhitungan luas persegi
elif selected == "Persegi":
    st.header("Hitung Luas Persegi")

    panjang_sisi = st.number_input("Masukkan Panjang Sisi", 0)
    hitung_persegi = st.button("Hitung Luas")

    if hitung_persegi:
        luas = panjang_sisi ** 2
        st.success(f"Luas Persegi = {luas}")
