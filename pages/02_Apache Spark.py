import streamlit as st
from PIL import Image

st.set_page_config(page_title="Apache Spark", page_icon=":house:")

image = Image.open("./src/img/Apache.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)