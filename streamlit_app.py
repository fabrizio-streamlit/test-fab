import streamlit as st
from io import StringIO

st.logo(
    image="https://i.ytimg.com/vi/8UtWJ5CVubg/maxresdefault.jpg",
    size="large"
)
fl = st.file_uploader(label="Carica Immagine")
caratteristiche = st.text_area(label='Caratteristiche',placeholder='Inserisci testo')

if st.button(label="Crea Descrizione"):
    if (caratteristiche != "") and (fl is not None):
        st.write('Elaborazione completata')
    else:
        if fl is None:
            st.toast('Immagine non inserita')
        else:
            st.toast('Caratteristiche non inserite')

if fl is not None:
    # To read file as bytes:

    bytes_data = fl.getvalue()
    st.write("filename:", fl.name)
    st.image(bytes_data)



