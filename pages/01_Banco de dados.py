import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banco de dados", page_icon=":house:")

image = Image.open("./src/img/Dados.jpg")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["AWS","Dicionario","Objetivos"])

with tab1:
        st.write("Oi")