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

    
   
    ## Lições Aprendidas e o Caminho a Seguir:

    Em resumo, a análise abrangente da PNAD 2020 revelou insights valiosos sobre o impacto da COVID-19 no Brasil. Identificamos padrões distintos em gênero, localização geográfica, sintomas clínicos e faixa etária, fornecendo uma base sólida para a formulação de estratégias de intervenção mais direcionadas.

    A aplicação de algoritmos como o K-Means trouxe uma compreensão mais refinada, destacando agrupamentos com propensões diferentes para internação. Estes grupos, oferecem insights valiosos para a priorização de recursos e estratégias.  Com este foco, estamos melhor posicionados para desenvolver políticas mais direcionadas e eficazes, principalmente para ações com o intuito de lidar com o grupo de maior risco: idosos e adultos ativos, pessoas que apresentavam mais de três sintomas, e dentre estes, sintomas respiratórios que classificamos como graves.

    Olhando para o futuro, esses resultados sugerem a necessidade contínua de abordagens interdisciplinares e adaptações metodológicas. A implementação de políticas públicas mais eficazes e equitativas requer uma compreensão mais profunda das nuances da disseminação do vírus.

    Em meio aos desafios, a riqueza de dados da PNAD 2020 abre portas para investigações mais aprofundadas e aprimoramento das estratégias existentes. Ao avançarmos, a combinação de tecnologia, análise de dados e colaboração interdisciplinar certamente impulsionará nossa capacidade de enfrentar futuras crises de saúde com resiliência e eficácia. 

    ## Ações Recomendadas:

    Com base em nosso entendimento, aqui estão algumas ações que o hospital pode considerar caso enfrentemos um novo surto da doença:

    1. **Preparação de Recursos**: Identificado o grupo 2, conforme citado acima, como o mais requisitante de atendimento hospitalar e vulnerável à internação, o hospital deve garantir que os recursos médicos estejam prontamente disponíveis para eles, como materiais adequados e pessoal capacitado; 
    2. **Campanhas de Conscientização**: Direcionar campanhas educativas para maior adesão às medidas preventivas de contaminação do vírus;
    3. **Parcerias com Planos de Saúde**: Estabelecer parcerias estratégicas com provedores de planos de saúde para garantir tratamento oportuno, já que pela amostra da população de infectados internados, apenas 28,24% possuíam este benefício,
    4. **Monitoramento Contínuo**: Utilizar dados em tempo real para monitorar o comportamento dos pacientes em relação à evolução da doença e adaptar estratégias conforme necessário.
            
    ### **Convite:**  
    A pandemia nos ensinou a importância da preparação e da adaptabilidade. Com os insights que agora possuímos, estamos melhor equipados para enfrentar desafios futuros. Convido você a continuar trabalhando conosco, usando o conhecimento adquirido para criar um futuro mais seguro e saudável para todos.

    **Obrigado por nos acompanhar nesta jornada. Juntos, podemos fazer a diferença.**
""")