import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sobre", page_icon=":house:")

image = Image.open("./src/img/Fiap.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("""
        # Sobre o Projeto

        Este projeto foi desenvolvido como parte do 3º Tech Challenge da turma de Data Science da FIAP. Foi uma oportunidade incrível para aprimorar nossas habilidades em análise de dados e colaboração em equipe, e gostaríamos de expressar nossa gratidão a todos que participaram deste desafio.

        ## Equipe do Projeto 

        - Amanda Bueno de Oliveira
        - João Guilherme Simões
        - Luiz Antonio Simette de Mello Campos
        - Paulo Henrique Barbosa Ortiz de Souza
                

        ## Orientadores 

        Este projeto não teria sido possível sem a orientação de nossos professores:

        - Edgard Joseph Kiriyama
        - Matheus Pavani

        Eles nos forneceram a estrutura necessária para concluir este desafio e estamos profundamente gratos pelo tempo e esforço que dedicaram à nossa aprendizagem.

        ##  Agradecimentos

        Também gostaríamos de agradecer aos nossos colegas de classe e a todos os envolvidos na organização deste desafio.

        ## Referências 📚

        **Guangyang Li. Documentação do pywaffle**. Disponível em: https://pywaffle.readthedocs.io/en/latest/index.html. Acesso em: 12 de Outubro de 2023.
                
        **DAITYARL, Shaumik . Cluster Analysis in Python**. DataCamp, 2023. Disponível em: https://app.datacamp.com/learn/courses/cluster-analysis-in-python. Acesso em: 23 de outubro de 2023.

        **Documentação do Streamlit**. Disponível em: https://docs.streamlit.io/. Acesso em: 12 de Outubro de 2023. 
        
        **Documentação do Apache Spark**. Disponível em: https://spark.apache.org/documentation.html. Acesso em: 01 de Outubro de 2023.
        
        **Imagem de capa das paginas gerados via IA Dalle-3**. Disponível em: https://www.bing.com/images/create/?ref=hn. Acesso em: 20 de outubro de 2023. 
        
        
            
        Gostaríamos de expressar nossa gratidão a todas estas fontes por disponibilizar esses dados publicamente.
        """, unsafe_allow_html=True)
