import streamlit as st
from PIL import Image

st.set_page_config(page_title="K-means", page_icon=":house:")

image = Image.open("./src/img/Model.jpg")
imageCorrelacao = Image.open("./src/img/Kmeans/Correlacao_PNAD.png")
imageEscolha = Image.open("./src/img/Kmeans/Escolha_numero_grupos_K-means.png")
imageGrupo = Image.open("./src/img/Kmeans/Agrupamento_K-means.png")
imageInternacaoIdade =Image.open("./src/img/Kmeans/Internacoes_e_faixa_etaria_por_grupo.png")
imageInternacaoGrave =Image.open("./src/img/Kmeans/Internacoes_e_sintomas_graves_por_grupo.png")
imageInternacaoGrupo =Image.open("./src/img/Kmeans/Internacoes_por_grupo.png")
imageInternacaoSintomas =Image.open("./src/img/Kmeans/Internacoes_por_quant_sintomas.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Inicio","Correlação","Componentes Principais","Qtd de grupos","Grupos formados", "Validação"])


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
        
        - **internou**: se o paciente foi internado e/ou entubado ou não;
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
        st.image(imageEscolha, caption="Gráfico para escolha de agrupamento.")
        
        st.markdown("""
        Como podemos observar, o número de grupos a serem formados pelo K-means são **3 grupos**.
        
        ## Explorando insights profundos com o K-Means

        Agora que identificamos o número ideal de clusters, é hora de aplicar o algoritmo K-Means e revelar os padrões ocultos em nossos dados.
        
        """)

with tab5:
        st.markdown("""
        # Analizando os grupos formados

        De acordo com o gráfico de dispersão que contém as duas primeiras componentes principais, pode-se afirmar que o algoritmo K-Means conseguiu identificar 3 grupos de maneira satisfatória, uma vez que os dados estão bem distribuídos em relação aos grupos e aos centróides, que se encontram de forma geral na posição central de cada grupo, ou onde há a presença de maior densidade dos dados.
        Há uma pequena sobreposição de alguns dos dados dos grupos de cor cinza e azul. Esse fato pode ser explicado pelas limitações do K-means, em virtude, por exemplo, das variáveis em sua essência serem categóricas e o algoritmo sensível a escala das variáveis. O K-means utiliza distâncias euclidianas para medir a dissimilaridade entre pontos de dados. Isso pode ser inadequado para variáveis categóricas, pois as distâncias euclidianas podem não refletir adequadamente a similaridade entre categorias em alguns casos.
        Vale salientar também que a interpretação gráfica dos resultados dos clusters formados pelo K-means neste caso não é direta/prática como aplicado à variáveis numéricas.             
        """)
        st.image(imageGrupo, caption="Gráfico dos grupo formados.")
        st.markdown("""
        ## Grafico de internações por grupos
        Após execução do modelo do kmeans sobre os dados da pesquisa dos individuos que procuraram alguma estabelecimento de saúde, fomos capazes de indentificar três perfils de individuos com diferentes probabilidades de internação/entubação , sendo capaz de dar maior luz de priorização de atendimento aqueles que possuem maior probabilidade de internação (grupo3), conforme analise abaixo: 
        """)
        st.image(imageInternacaoGrupo, caption="Gráfico dos internações por grupo.")
        st.markdown("""
        ## Gráfico de distribuição de Quantidade de sintomas por grupo:
        Analisamos como estavam distribuidos a quantidade de sintomas nos casos de internação por grupo, e verificamos que praticamente 100% dos casos de internação do Grupos 2 tem 3 ou mais sintomas, conforme gráfico abaixo:
        """)
        st.image(imageInternacaoSintomas, caption="Gráfico dos internações por quantidades de Sitomas de cada grupo.")
        st.markdown("""
        ## Gráfico de distribuição de idade por grupo:
        Analisamos as internações por faixa de idade em cada grupo, e verificamos que os grupos 1 e 2 possuem alto representatividade de Idosos (>60 anos)  e adultos e fase ativa (31 - 60 anos)
        """)
        st.image(imageInternacaoIdade, caption="Gráfico de internações por Idade de cada grupo.")
        st.markdown("""
        ## Gráfico de distribuição de sintomas Graves por grupos:
        Analisamos a distribuição de sintomas graves (Falta de ar, fadiga e dor no peito) entre os grupos e notamos que o grupo 2, cerca de 96% dos pacientes internados apresentavam tais sintomas.
        """)
        st.image(imageInternacaoGrave, caption="Gráfico dos internações por Sitomas grave de cada grupo.")
        

with tab6:
        
        st.markdown("""
        
        # Métrica de Validação Silhouette Score
        
        O Silhouette Score é uma métrica de avaliação de clusterização utilizada para determinar a qualidade da separação de dados em clusters. Ele fornece uma medida de quão bem os objetos em um cluster estão agrupados em relação a objetos de outros clusters. Em outras palavras, o Silhouette Score avalia a coesão intra-cluster e a separação inter-cluster.
        
        O Silhouette Score varia de -1 a +1, com valores mais altos indicando uma clusterização melhor. Um valor próximo de +1 indica que os objetos dentro do cluster estão bem agrupados e separados de outros clusters, enquanto um valor próximo de **-1** sugere que a clusterização está inadequada, e os objetos podem estar melhor em clusters diferentes. 
        Um valor próximo de 0 indica que a sobreposição entre clusters pode estar ocorrendo.
        
        A métrica Silhouette Score resultante da modelagem K-Means dos nossos dados foi de **0,3380**, relativamente alta e indica que a clusterização dos dados é boa. Geralmente, valores do Silhouette Score no intervalo de **0,25 a 0,5** são considerados bons, pois sugerem que os objetos dentro dos clusters estão bem agrupados e que há uma separação adequada entre os clusters.        
        
        ## Outras métricas de amparo 
        
        Podem ser utilizadas ainda outras métricas de validação para a análise de agrupamento, como Calinski-Harabasz Score e Davies-Bouldin Score. 
        
        Calinski-Harabasz Score: Esta métrica avalia a separação entre os clusters e a compactação dos pontos de dados dentro dos clusters. 
        Quanto maior o valor, melhor a qualidade do agrupamento, indicando clusters bem definidos e compactos. O Calinski-Harabasz Score para nosso modelo foi de **4224,57**, o que simboliza um agrupamento de alta qualidade, com pontos de dados bem agrupados e clusters bem definidos.
        
        Davies-Bouldin Score: Esta métrica mede a dissimilaridade média entre cada cluster e seu cluster mais semelhante. Um valor mais baixo indica uma melhor separação entre os clusters e, portanto, um agrupamento de maior qualidade. Nosso agrupamento dos dados apresentou **Davies-Bouldin Score igual a 1,25**, indicando que a dissimilaridade entre os clusters é relativamente pequena em comparação com a dissimilaridade dentro dos clusters.
                    
        """)
