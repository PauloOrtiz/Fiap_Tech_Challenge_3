import streamlit as st
from PIL import Image

st.set_page_config(page_title="K-means", page_icon=":house:")

image = Image.open("./src/img/Model.jpg")
imageCorrelacao = Image.open("./src/img/Dash/Kmeans/Correlacao_PNAD.png")
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
        st.markdown("""
        # Correlação em K-Means

        A análise de correlação é uma ferramenta poderosa para identificar relações entre variáveis. No contexto do K-Means, a correlação nos ajuda a entender como diferentes características se relacionam entre si dentro dos clusters formados. Ao identificar correlações fortes, podemos obter insights valiosos sobre padrões ocultos nos dados e tomar decisões informadas.

        ## Análise de Correlação

        Observando o gráfico de correlação, notamos algumas relações interessantes. A contagem de sintomas apresenta uma forte relação com a ida a um estabelecimento de saúde. Isso sugere que, quanto mais sintomas um indivíduo apresenta, maior é a probabilidade de ele buscar atendimento médico. Além disso, há uma forte correlação entre os sintomas, indicando que os pacientes que apresentaram sintomas geralmente tiveram mais de um sintoma simultaneamente.
        """)

        st.image(imageCorrelacao, caption="Gráfico de Correlação dos Sintomas e Atendimento Médico.")

        st.markdown("""
        ### Conclusão

        Através desta análise de correlação, conseguimos identificar padrões claros nos dados. A forte relação entre a contagem de sintomas e a busca por atendimento médico reforça a importância de monitorar e tratar os sintomas precocemente. Além disso, a correlação entre os sintomas sugere que a COVID-19 pode manifestar-se de várias maneiras em um paciente, tornando ainda mais crucial a conscientização sobre todos os possíveis sintomas da doença. À medida que avançamos, esses insights nos ajudarão a desenvolver estratégias mais eficazes para lidar com futuros surtos e melhorar o atendimento ao paciente.

        """)

with tab3:
        pass

with tab4:
        pass

with tab5:
        pass

