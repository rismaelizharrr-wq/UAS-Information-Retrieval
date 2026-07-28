import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Scraping", page_icon="📚")

st.title("📚 Hasil Web Scraping Buku")

# Membaca data
df = pd.read_csv("books.csv")

st.success(f"Jumlah data: {len(df)} buku")

# Pencarian buku
st.subheader("🔎 Cari Buku")

keyword = st.text_input("Masukkan judul buku")

if keyword:
    hasil = df[df["title"].str.contains(keyword, case=False, na=False)]

    st.write(f"Ditemukan {len(hasil)} buku")

    st.dataframe(hasil)
else:
    st.dataframe(df)