import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banco de dados", page_icon=":house:")

image = Image.open("./src/img/Dados.png")
image2 = Image.open("./src/img/AWS.jpg")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["PNAD Covid-19","AWS","Dicionário"])

with tab1:
        pass


with tab2:

        st.markdown("""
        # Dicionário de Dados: Navegando pelas Colunas do PNAD-COVID-19

        A base de dados do PNAD-COVID-19 do IBGE é vasta e rica em detalhes. Para nossa análise, focamos em colunas específicas que nos ajudariam a entender melhor o impacto e as implicações da pandemia. Vamos explorar essas colunas, organizadas por categorias.

        ## Dados Padrão (Informações Pessoais)

        Estas são as colunas que contêm informações básicas sobre os respondentes. Elas não são contadas como perguntas, mas são essenciais para contextualizar e segmentar as respostas.

        | Nome da Coluna | Descrição |
        | -------------- | --------- |
        | uf | Unidade da Federação |
        | tipo_domicilio | Situação do domicílio |
        | sexo | Sexo |
        | cor | Cor ou raça |
        | escolaridade | Escolaridade |

        ## Trilha dos Sintomas Clínicos

        Estas colunas nos ajudam a entender os sintomas clínicos apresentados pelos respondentes durante a pandemia.

        | Número Pergunta | Nome da Coluna | Descrição |
        | --------------- | -------------- | --------- |
        | 1 | sintoma_febre | Na semana passada teve febre? |
        | 2 | sintoma_tosse | Na semana passada teve tosse? |
        | 3 | sintoma_dor_garganta | Na semana passada teve dor de garganta? |
        | 4 | sintoma_dificuldade_respirar | Na semana passada teve dificuldade para respirar? |
        | 5 | sintoma_dor_cabeca | Na semana passada teve dor de cabeça? |
        | 6 | sintoma_dor_peito | Na semana passada teve dor no peito? |
        | 7 | sintoma_nausea | Na semana passada teve náusea? |
        | 8 | sintoma_nariz_entupido_escorrendo | Na semana passada teve nariz entupido ou escorrendo? |
        | 9 | sintoma_fadiga | Na semana passada teve fadiga? |
        | 10 | sintoma_perda_cheiro_sabor | Na semana passada teve perda de cheiro ou sabor? |
        | 11 | sintoma_dor_muscular | Na semana passada teve dor muscular? |
        | 12 | sintoma_diarreia | Na semana passada teve diarreia? |
        | 13 | usou_respiracao_artificial | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |

        ## Trilha do Comportamento da População

        Estas colunas nos dão insights sobre como a população reagiu e se comportou durante a pandemia.

        | Número Pergunta | Nome da Coluna | Descrição |
        | --------------- | -------------- | --------- |
        | 15 | isolamento | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
        | 17 | fez_home_office | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |

        ## Trilha Econômica

        Estas colunas nos ajudam a entender os impactos econômicos da pandemia sobre os respondentes.

        | Número Pergunta | Nome da Coluna | Descrição |
        | --------------- | -------------- | --------- |
        | 14 | tem_plano_saude | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
        | 16 | faixa_rendimento | Número da faixa do rendimento/retirada em dinheiro |
        | 18 | recebeu_auxilio | Auxílios emergenciais relacionados ao coronavirus |

                    
        Acompanhe-nos nesta jornada enquanto mergulhamos profundamente em cada uma dessas colunas, desvendando as histórias e insights que elas têm a nos contar.
        
        ### Próximos Passos

        Agora que estamos familiarizados com a estrutura do banco de dados e as perguntas cruciais que escolhemos analisar, é hora de mergulhar mais fundo. A verdadeira magia acontece quando transformamos esses dados em insights acionáveis.

        Convido você a continuar esta aventura explorando a análise exploratória. Você encontrará essa seção no menu à esquerda. Juntos, vamos descobrir as histórias ocultas nos dados e, quem sabe, encontrar respostas para algumas das perguntas mais prementes desta pandemia.

        **Vamos lá? A jornada apenas começou!**
                    
        """)

with tab3:
        st.markdown("""
        # Armazenamento e Análise de Dados na AWS

        Os dados do PNAD, juntamente com fontes auxiliares, foram armazenados na **Amazon S3**, onde estabelecemos a camada de dados brutos (Bronze Data). Essa camada contém dados não processados ou sem intervenção manual, todos disponíveis na nuvem.

        A partir desses dados brutos, conduzimos os processos iniciais de tratamento de dados. Devido ao grande volume de dados, optamos por usar a **Amazon EC2** em conjunto com o **PySpark** para garantir um desempenho superior. Isso resultou na criação de uma nova camada de dados, agora tratados (Silver Data), que foi disponibilizada no bucket da Amazon S3.

        As análises e explorações desses dados foram conduzidas usando o **Amazon Redshift**, através de consultas SQL, e a **Amazon EC2**, com a linguagem Python e o Spark. Essa etapa resultou na criação da camada final de dados, que será apresentada na aplicação Streamlit. Nessa aplicação, os resultados das análises e explorações de dados serão exibidos de forma acessível e informativa.

        ## Aplicações utilizadas:

        - **Amazon S3**— O Amazon Simple Storage Service (Amazon S3) é um serviço de armazenamento de objetos altamente escalável. O Amazon S3 pode ser usado para uma ampla variedade de soluções de armazenamento, incluindo sites, aplicativos móveis, backups e data lakes.

        - **Amazon Redshift**— O Amazon Redshift é um serviço de armazenamento de dados totalmente gerenciado em escala de petabytes. Com o Amazon Redshift, você pode consultar petabytes de dados estruturados e semiestruturados em seu data warehouse e em seu data lake usando SQL padrão.

        - **Amazon EC2**— Amazon Elastic Compute Cloud (EC2) é uma parte central da plataforma de cloud computing da Amazon.com, Amazon Web Services (AWS). O EC2 permite que os usuários aluguem computadores virtuais nos quais rodam suas próprias aplicações. O EC2 permite a implantação de aplicações escaláveis ao prover um Web service através do qual um usuário pode iniciar uma Amazon Machine Image para criar uma máquina virtual.
        """)
        st.image(image2)
