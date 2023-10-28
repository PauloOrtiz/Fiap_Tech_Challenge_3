import streamlit as st
from PIL import Image

st.set_page_config(page_title="K-means", page_icon=":house:")

image = Image.open("./src/img/Model.jpg")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introdução","Análise de Correlação","Quantidade de grupos","Grupos formados", "Validação do modelo"])


with tab1:
        pass

with tab2: 
        pass

with tab3:
        pass

with tab4:
        pass

with tab5:
        pass

