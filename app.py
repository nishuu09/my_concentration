import streamlit as st

st.set_page_config(page_title="Konversi Berat", layout="centered")

st.title("⚖️ Konversi Berat")
st.markdown("Konversi antara satuan berat: kilogram, gram, pound, dan ounce.")

# Dictionary konversi ke kilogram
conversion_factors = {
    'Kilogram (kg)': 1,
    'Gram (g)': 0.001,
    'Pound (lb)': 0.453592,
    'Ounce (oz)': 0.0283495
}

# Input dari pengguna
weight = st.number_input("Masukkan berat", min_value=0.0, format="%.4f")

from_unit = st.selectbox("Dari satuan", list(conversion_factors.keys()))
to_unit = st.selectbox("Ke satuan", list(conversion_factors.keys()))

if st.button("Konversi"):
    # Konversi ke kilogram dulu
    weight_kg = weight * conversion_factors[from_unit]
    # Lalu ke satuan tujuan
    converted = weight_kg / conversion_factors[to_unit]
    st.success(f"{weight} {from_unit} = {round(converted, 4)} {to_unit}")
