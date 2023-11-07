import streamlit as st
from PIL import Image

st.set_page_config(page_title="Conclusão", page_icon=":house:")

image = Image.open("./src/img/Conclusao.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
    # Conclusão: Navegando Rumo ao Futuro

    Após nossa jornada profunda pelos mares de dados, emergimos com uma compreensão clara do perfil da população e dos grupos distintos que a compõem. Cada grupo, com suas características únicas, nos contou uma história, revelando nuances sobre como a pandemia afetou diferentes segmentos da sociedade.

    ## Ações Recomendadas:

    Com base em nosso entendimento, aqui estão algumas ações que o hospital pode considerar caso enfrentemos um novo surto da doença:

    1. **Preparação de Recursos**: Identificar os grupos mais vulneráveis e garantir que os recursos médicos estejam prontamente disponíveis para eles.
    2. **Campanhas de Conscientização**: Direcionar campanhas educativas para grupos que mostraram menor adesão às medidas preventivas.
    3. **Parcerias com Planos de Saúde**: Estabelecer parcerias estratégicas com provedores de planos de saúde para garantir tratamento oportuno.
    4. **Monitoramento Contínuo**: Utilizar dados em tempo real para monitorar a situação e adaptar estratégias conforme necessário.

    ## Resultados:

    *Aqui, incluiremos os resultados específicos e insights obtidos a partir das análises.*

    **Convite:**  
    A pandemia nos ensinou a importância da preparação e da adaptabilidade. Com os insights que agora possuímos, estamos melhor equipados para enfrentar desafios futuros. Convido você a continuar trabalhando conosco, usando o conhecimento adquirido para criar um futuro mais seguro e saudável para todos.

    **Obrigado por nos acompanhar nesta jornada. Juntos, podemos fazer a diferença.**
""")