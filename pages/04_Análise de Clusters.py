import streamlit as st
from PIL import Image

st.set_page_config(page_title="Análise de Clusters", page_icon=":house:")

image = Image.open("./src/img/Cluster.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
    # Análise de Agrupamento: Revelando Padrões Ocultos

    Imagine que você está em uma sala escura, tentando entender a disposição dos objetos nela. Você sente formas, tamanhos e texturas diferentes, mas não consegue ver o todo. Agora, imagine que uma luz suave se acende, revelando grupos de objetos semelhantes agrupados juntos. Esta é a magia da análise de agrupamento.

    ## O que é Análise de Agrupamento?

    A análise de agrupamento, ou *clustering*, é uma técnica de aprendizado de máquina não supervisionada que visa identificar e agrupar dados semelhantes com base em características específicas. Em outras palavras, ela busca padrões nos dados e agrupa pontos de dados semelhantes juntos, revelando estruturas ocultas e insights valiosos.

    ## Quando Usar a Análise de Agrupamento?

    Esta análise é particularmente útil quando não temos rótulos pré-definidos para nossos dados e queremos entender a estrutura intrínseca deles. Pode ser usada para segmentação de clientes, detecção de anomalias, organização de conteúdo e muito mais.

    ## Algoritmos Comumente utilizados:

    - **K-means**: Um dos algoritmos mais populares, ele tenta encontrar 'k' centróides e atribui cada ponto de dados ao centróide mais próximo. É eficaz e eficiente para grandes conjuntos de dados, mas o número 'k' de clusters deve ser especificado antecipadamente.

    - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: Este algoritmo agrupa pontos que estão próximos em termos de densidade e pode identificar clusters de forma e tamanho variáveis. Uma grande vantagem é que ele pode identificar pontos de ruído no conjunto de dados.
    
     - **Hierarchical Clustering**: Este algoritmo agrupa pontos de dados em uma hierarquia de clusters, começando com clusters individuais e combinando-os em clusters maiores. Ele pode ser usado para identificar clusters de diferentes tamanhos e formas.

    - **Gaussian Mixture Model (GMM)**: Este algoritmo assume que os pontos de dados são gerados a partir de uma mistura de distribuições gaussianas e tenta encontrar as distribuições subjacentes. É útil para identificar clusters com diferentes formas e tamanhos.

    - **Agglomerative Clustering**: Este algoritmo começa com cada ponto de dados como seu próprio cluster e, em seguida, combina os clusters mais próximos até que todos os pontos de dados estejam em um único cluster. Ele pode ser usado para identificar clusters de diferentes tamanhos e formas.

    **Convite:**  
    Com a análise de agrupamento como nossa bússola, vamos desvendar os padrões ocultos nos dados, descobrindo histórias e insights que aguardam para serem revelados.

    **Está pronto para ver a sala escura dos dados iluminada?**
""")