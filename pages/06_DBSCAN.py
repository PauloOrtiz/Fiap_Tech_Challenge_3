import streamlit as st
from PIL import Image

st.set_page_config(page_title="DBSCAN", page_icon=":house:")

image = Image.open("./src/img/DBSCAN.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


tab1, tab2, tab3= st.tabs(["Introdução","Grupos","DBSCAN x K-Means"])


with tab1:
    st.markdown("""
    # DBSCAN: Descobrindo Constelações nos Dados

    Imagine que você está olhando para o céu noturno, tentando identificar constelações. Algumas estrelas estão próximas umas das outras, formando padrões claros, enquanto outras estão isoladas, perdidas na vastidão do espaço. O DBSCAN é como um astrônomo experiente, identificando constelações nos seus dados.

    ## Como funciona o DBSCAN?

    O DBSCAN, ou "Density-Based Spatial Clustering of Applications with Noise", funciona identificando áreas de alta densidade que são separadas por áreas de baixa densidade. Ao contrário do K-means, que se concentra em agrupamentos esféricos, o DBSCAN pode identificar clusters de formas variáveis. Ele agrupa pontos que estão próximos em termos de densidade e marca pontos isolados como "ruído".

    ## Vantagens e Desvantagens:

    **Vantagens**:
    - Pode identificar clusters de formas e tamanhos variáveis.
    - Não requer a especificação do número de clusters.
    - Pode identificar pontos de ruído no conjunto de dados.

    **Desvantagens**:
    - Pode ter dificuldade quando os clusters têm densidades variáveis.
    - Sensível aos parâmetros de entrada.

    ## Por que DBSCAN neste projeto?

    Em nossa busca por entender os intricados padrões da pandemia, queríamos uma abordagem que pudesse identificar grupos naturais nos dados, sem ser restringida por formas predefinidas. O DBSCAN, com sua capacidade de identificar clusters de formas variáveis, foi uma escolha lógica. Além disso, ao compará-lo com o K-means, buscamos uma maior confiabilidade na formação dos grupos, garantindo que nossos insights sejam tanto precisos quanto profundos.

    """)

with tab2: 
        pass

with tab3:
        pass



