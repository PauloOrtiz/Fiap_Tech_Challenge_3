import streamlit as st
from PIL import Image

st.set_page_config(page_title="K-means", page_icon=":house:")

image = Image.open("./src/img/Model.jpg")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introdução","Análise de Correlação","Quantidade de grupos","Grupos formados", "Validação do modelo"])


with tab1:
        st.markdown("""
        # K-means: A Arte de Segmentar

        Imagine que você está em um grande salão de festas, com pessoas de todas as idades, profissões e interesses. Seu desafio é organizar pequenos grupos de conversa, onde cada pessoa tem algo em comum com os outros membros do seu grupo. Como você faria isso? O algoritmo K-means pode ser sua solução!

        ## Como funciona o K-means?

        O K-means é como um maestro habilidoso que organiza uma orquestra. Ele começa escolhendo 'k' pontos aleatórios (nossos maestros) e atribui cada membro da orquestra (ponto de dados) ao maestro mais próximo, com base em suas características. Em seguida, ele recalcula a posição do maestro com base nos membros de sua seção e repete o processo até que a orquestra esteja harmoniosamente organizada em 'k' seções.

        ## Vantagens e Desvantagens:

        **Vantagens**:
        - Simplicidade e eficiência, tornando-o adequado para grandes conjuntos de dados.
        - Resultados interpretáveis e fáceis de entender.

        **Desvantagens**:
        - O número 'k' de clusters deve ser definido antecipadamente.
        - Sensível à inicialização, podendo cair em mínimos locais.
        - Pode ter dificuldade com clusters de formas não esféricas.

        ## Por que K-means neste projeto?

        Em nossa missão de entender a pandemia, queremos segmentar a população de pacientes em grupos distintos. O K-means nos permite identificar similaridades entre os pacientes, agrupando-os de forma que cada grupo revele padrões e tendências específicas. Assim, podemos obter insights mais profundos sobre diferentes segmentos da população e adaptar estratégias de intervenção de acordo.
        
        """)


with tab2: 
        pass

with tab3:
        pass

with tab4:
        pass

with tab5:
        pass

