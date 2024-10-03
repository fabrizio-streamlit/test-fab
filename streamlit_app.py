import streamlit as st
from io import StringIO

st.logo(
    image="https://i.ytimg.com/vi/8UtWJ5CVubg/maxresdefault.jpg",
)
fl = st.file_uploader(label="Carica Immagine")
caratteristiche = st.text_area(label='Caratteristiche',placeholder='Inserisci testo')


if fl is not None:
    # To read file as bytes:

    bytes_data = fl.getvalue()
    st.write("filename:", fl.name)
    st.image(bytes_data)



