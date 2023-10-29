import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banco de dados", page_icon=":house:")

image = Image.open("./src/img/Dados.png")
image2 = Image.open("./src/img/AWS.jpg")
image3 = Image.open("./src/img/Dash/Estrutura_DB.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["PNAD Covid-19","Dicionário","AWS"])

with tab1:
        st.markdown("""
        # PNAD Covid: Uma Lente Sobre a Pandemia no Brasil

        Em tempos de incertezas e desafios, a informação é a chave para a tomada de decisões informadas. E é aqui que entra o **PNAD Covid**.

        ## O que é o PNAD Covid?

        O PNAD Covid, ou Pesquisa Nacional por Amostra de Domicílios - COVID-19, é mais do que apenas uma pesquisa. É uma iniciativa do Instituto Brasileiro de Geografia e Estatística (IBGE) que busca entender os profundos efeitos da pandemia em nosso país. Através de questionários detalhados, domicílios de todo o Brasil compartilham suas experiências, desafios e realidades, fornecendo um panorama abrangente da situação atual.

        ## Quais são os objetivos da pesquisa?

        A missão da PNAD COVID-19 é vasta. Ela busca mensurar o impacto da pandemia no mercado de trabalho brasileiro, entender as mudanças na renda da população e, crucialmente, coletar informações sobre os sintomas referidos que poderiam estar associados à COVID-19. Além disso, a pesquisa lança luz sobre tópicos cruciais como a prevalência da testagem positiva para o vírus, a transição para o trabalho em "home office" e a influência vital do auxílio emergencial na economia doméstica.

        ## Qual sua importância?

        Imagine navegar por um oceano tempestuoso sem um mapa ou bússola. Assim seria nosso enfrentamento à pandemia sem o PNAD Covid. Esta pesquisa é nossa bússola, guiando-nos através dos mares turbulentos da crise sanitária. Ela nos oferece insights valiosos sobre a realidade da população, permitindo que formuladores de políticas, profissionais de saúde e a sociedade em geral tomem decisões mais informadas e eficazes.

        ---

        **Convite:**  
        Convido você a se juntar a nós nesta jornada de descoberta. Com o PNAD Covid como nosso guia, vamos explorar os cantos e recantos da pandemia no Brasil, desvendando as histórias ocultas nos dados e buscando soluções para os desafios que enfrentamos.

        **Está pronto para a jornada?**
        """)

with tab2:
        
        st.markdown("""
        ## Dicionário de Dados: Navegando pelas Colunas do PNAD-COVID-19

        A base de dados do PNAD-COVID-19 do IBGE é vasta e rica em detalhes. Para nossa análise, focamos em colunas específicas que nos ajudariam a entender melhor o impacto e as implicações da pandemia. Vamos explorar essas colunas, organizadas por categorias.

        ### Dados Padrão (Informações Pessoais)

        Estas são as colunas que contêm informações básicas sobre os respondentes. Elas não são contadas como perguntas, mas são essenciais para contextualizar e segmentar as respostas.

        | Campo | Descrição |
        | ----- | --------- |
        | UF | Unidade da Federação |
        | CAPITAL | Capital |
        | RM_RIDE | Região Metropolitana e Região Administrativa Integrada de Desenvolvimento |
        | V1012 | Semana no mês |
        | V1013 | Mês da pesquisa |
        | V1022 | Situação do domicílio |
        | V1023 | Tipo de área |
        | A002 | Idade do morador |
        | A003 | Sexo |
        | A004 | Cor ou raça |
        | A005 | Escolaridade |

        ### Perguntas Clínicas e Comportamentais

        Estas colunas nos ajudam a entender os sintomas clínicos apresentados pelos respondentes durante a pandemia, bem como seus comportamentos e atitudes.

        | Pergunta | Campo | Descrição |
        | -------- | ----- | --------- |
        | 1 | B0011 | Na semana passada teve febre? |
        | 2 | B0012 | Na semana passada teve tosse? |
        | 3 | B0013 | Na semana passada teve dor de garganta? |
        | 4 | B0014 | Na semana passada teve dificuldade para respirar? |
        | 5 | B0015 | Na semana passada teve dor de cabeça? |
        | 6 | B0016 | Na semana passada teve dor no peito? |
        | 7 | B0017 | Na semana passada teve náusea? |
        | 8 | B0018 | Na semana passada teve nariz entupido ou escorrendo? |
        | 9 | B0019 | Na semana passada teve fadiga? |
        | 10 | B00110 | Na semana passada teve dor nos olhos? |
        | 11 | B00111 | Na semana passada teve perda de cheiro ou sabor? |
        | 12 | B00112 | Na semana passada teve dor muscular? |
        | 13 | B00113 | Na semana passada teve diarreia? |
        | 14 | B002 | Por causa disso, foi a algum estabelecimento de saúde? |
        | 15 | B006 | Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador |
        | 16 | B007 | Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público |
        | 17 | B009B | Qual o resultado? (SWAB) |
        | 18 | B011 | Na semana passada, devido à pandemia do Coronavírus, em que medida o(a) Sr(a) restringiu o contato com as pessoas? |
        | 19 | C013 | Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)? |
        | 20 | D0051 | Auxílios emergenciais relacionados ao coronavirus |

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

        st.markdown("""
        ## Estrutura do Banco de Dados

        Agora que entendemos como os dados foram armazenados e processados, é crucial compreender a estrutura do banco de dados. A estrutura nos dá uma visão clara de como os dados estão organizados, facilitando a análise e a extração de insights valiosos.

        A seguir, apresentamos um esquema visual da estrutura do banco de dados, destacando as principais tabelas, relações e campos-chave. Esta visualização nos ajudará a navegar pelos dados com eficiência e precisão.
        """)
        st.image(image3)