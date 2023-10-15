import streamlit as st
from PIL import Image

st.set_page_config(page_title="Banco de dados", page_icon=":house:")

image = Image.open("./src/img/Dados.jpg")
image2 = Image.open("./src/img/AWS.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["AWS","Dicionario","Objetivos"])

with tab1:
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
