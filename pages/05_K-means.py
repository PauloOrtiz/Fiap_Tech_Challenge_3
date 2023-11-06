import streamlit as st
from PIL import Image

st.set_page_config(page_title="K-means", page_icon=":house:")

image = Image.open("./src/img/Model.jpg")
imageCorrelacao = Image.open("./src/img/Kmeans/Correlacao_PNAD.png")
imageEscolha = Image.open("./src/img/Kmeans/Escolha_numero_grupos_K-means.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Introdução","Análise de Correlação","Componentes Principais","Quantidade de grupos","Grupos formados", "Validação do modelo"])


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

       Em nossa missão de entender a pandemia, queremos segmentar a população de pacientes em grupos distintos. O K-means nos permite identificar similaridades entre os pacientes, agrupando-os de forma que cada grupo revele padrões e tendências específicas. Assim, podemos obter insights mais profundos sobre diferentes segmentos da população e adaptar estratégias de intervenção de acordo, respondendo a pergunta principal: dentre as pessoas que buscaram atendimento em alguma unidade hospitalar, como podemos identificar pacientes com maior chance de internação?
        
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
        st.markdown("""
        # A Maldição da Dimensionalidade dos dados
        
        À medida que a dimensionalidade dos dados aumenta, a densidade dos pontos de dados no espaço diminui, o que pode tornar os agrupamentos menos distintos e mais sensíveis a outliers. 
        
        Isso é conhecido como o "efeito da maldição da dimensionalidade" e pode afetar negativamente o desempenho do K-means.
        
        Com a finalidade de otimizar o modelo de agrupamento com os dados já conhecidos e solucionar o problema da maldição da dimensionalidade dos dados, selecionamos 7 variáveis para identificação dos pacientes com maior chance de serem internados, sendo elas: 
        
        - **internou**: se o paciente foi internado/entubado ou não;
        - **tem_plano_saude**: se o paciente possui plano de saúde ou não, pois através da análise exploratória identificamos que pacientes que não possuem plano de sáude são mais fragilizados, principalmente devido à exposição ao virus;
        - **qtd_sintomas**: se o paciente apresenta 0 sintomas, de 1 a 2 sintomas ou mais de 3 sintomas, para provarmos a ideia de que pacientes com maior número de sintomas possuem mais chances de internação;
        - **fx_idade**: faixa etária dos pacientes, sendo "0" menor de 12 anos (infantil), "1" de 12 a 17 anos (adolescentes), "2" de 18 a 30 anos (jovens), "3" de 30 a 59 anos (adultos) e "4" maior de 60 anos (idosos). Assim poderemos ver alguma relação da faixa etária em relação aos grupos formados pelo algoritmo.
        - **sintomas_graves**: pacientes que possuem os sintomas identificados como "graves" na análise exploratória: dificuldade para respirar, fadiga e dor no peito;
        - **sintomas_medios**: tosse, febre, dor muscular, dor de garganta e dor de cabeça;
        - **sintomas_leves**: outros sintomas.
        
        ## Análise de Componentes Principais
        
        Além da seleção das principais variáveis para o modelo, a Análise de Componentes Principais (PCA) se apresenta como outra solução para a maldição citada, reduzindo a dimensionalidade dos dados A PCA é uma técnica estatística comumente empregada como um passo prévio à aplicação de algoritmos de análise de agrupamento, como o K-Means, pois torna os dados complexos mais gerenciáveis e ajuda a melhorar o desempenho do modelo.
        
        Foram escolhidas 5 componentes principais para representar o conjunto de dados que continham as 7 variáveis mencionadas anteriormente. As componentes explicaram 86,9% da variabilidade dos dados originais.
        
        """)

with tab4:
        st.markdown("""
        # Elbow Plot            

        O gráfico Elbow, também conhecido como método do cotovelo, é uma ferramenta utilizada na análise de agrupamento (clustering) de dados. Ele ajuda a determinar o número ideal de clusters em um conjunto de dados quando se utiliza algoritmos de agrupamento, como o K-Means. 
        
        O nome "cotovelo" se deve à forma do gráfico, que se assemelha a um cotovelo dobrado. Para o nosso conjunto de dados, o gráfico se apresentou como se segue abaixo:
        
        """)
        st.image(imageCorrelacao, caption="Gráfico para escolha de agrupamento.")
        
        st.markdown("""
        Como podemos observar, o número de grupos a serem formados pelo K-means são 3 grupos.
        
        ## Explorando insights profundos com o K-Means

        Agora que identificamos o número ideal de clusters, é hora de aplicar o algoritmo K-Means e revelar os padrões ocultos em nossos dados.
        
        """)

with tab5:
        pass

with tab6:
        pass

