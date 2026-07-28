import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Search", layout="wide")

df = pd.read_csv("books.csv")

st.title("📚 Book Search (Scraped via Scrapy)")

query = st.text_input("Cari...")

if query:
    hasil = df[df["title"].str.contains(query, case=False, na=False)]
else:
    hasil = df

st.markdown(f"## ✨ Ditemukan {len(hasil)} hasil")

for _, row in hasil.iterrows():
    st.markdown(f"### [{row['title']}]({row['link']})")
    st.write(
        f"**Price:** {row['price']} | "
        f"**Rating:** {row['rating']} | "
        f"**Availability:** {row['availability']}"
    )
    st.divider()