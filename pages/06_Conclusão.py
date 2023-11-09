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

    

    ## Resultados:

    Em resumo, a análise abrangente da PNAD 2020 revelou insights valiosos sobre o impacto da COVID-19 no Brasil. Identificamos padrões distintos em gênero, localização geográfica e faixa etária, fornecendo uma base sólida para a formulação de estratégias de intervenção mais direcionadas.

    A aplicação de algoritmos como o K-Means trouxe uma compreensão mais refinada, destacando grupos com diferentes probabilidades de internação.Revelou nuances cruciais sobre o impacto da COVID-19, destacando grupos distintos através do K-Means. Estes grupos, identificados com diferentes probabilidades de internação, oferecem insights valiosos para a priorização de recursos e estratégias.  Ao focarmos nesses grupos específicos, estamos melhor posicionados para desenvolver políticas mais direcionadas e eficazes, principalmente para ações nos grupos de maior riscos como idosos e adultos ativos, pessoas com mais de três sintomas, e que apresentam sintomas respiratorios que classificamos como graves.

    Olhando para o futuro, esses resultados sugerem a necessidade contínua de abordagens interdisciplinares e adaptações metodológicas. A implementação de políticas públicas mais eficazes e equitativas requer uma compreensão mais profunda das nuances da disseminação do vírus.

    Em meio aos desafios, a riqueza de dados da PNAD 2020 abre portas para investigações mais aprofundadas e aprimoramento das estratégias existentes. Ao avançarmos, a combinação de tecnologia, análise de dados e colaboração interdisciplinar certamente impulsionará nossa capacidade de enfrentar futuras crises de saúde com resiliência e eficácia.

            
    ## Ações Recomendadas:

    Com base em nosso entendimento, aqui estão algumas ações que o hospital pode considerar caso enfrentemos um novo surto da doença:

    1. **Preparação de Recursos**: Identificar os grupos mais vulneráveis e garantir que os recursos médicos estejam prontamente disponíveis para eles.
    2. **Campanhas de Conscientização**: Direcionar campanhas educativas para grupos que mostraram menor adesão às medidas preventivas.
    3. **Parcerias com Planos de Saúde**: Estabelecer parcerias estratégicas com provedores de planos de saúde para garantir tratamento oportuno.
    4. **Monitoramento Contínuo**: Utilizar dados em tempo real para monitorar a situação e adaptar estratégias conforme necessário.
            
    ### **Convite:**  
    A pandemia nos ensinou a importância da preparação e da adaptabilidade. Com os insights que agora possuímos, estamos melhor equipados para enfrentar desafios futuros. Convido você a continuar trabalhando conosco, usando o conhecimento adquirido para criar um futuro mais seguro e saudável para todos.

    **Obrigado por nos acompanhar nesta jornada. Juntos, podemos fazer a diferença.**
""")