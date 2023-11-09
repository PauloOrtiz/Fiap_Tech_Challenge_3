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

    
   
    ## Conclusão: Lições Aprendidas e o Caminho a Seguir:

    À medida que encerramos nossa análise da PNAD 2020, emergimos com uma compreensão mais profunda do impacto da COVID-19. As histórias contadas pelos dados nos revelaram padrões e disparidades, iluminando o caminho para intervenções mais direcionadas e eficazes.

    ### O Poder da Segmentação com K-Means

    A aplicação do K-Means nos permitiu identificar grupos com riscos e necessidades distintas. Esta segmentação é crucial, pois nos permite focar nossos esforços nos grupos mais vulneráveis: idosos, adultos em idade ativa e aqueles com múltiplos sintomas graves.

    ### Estratégias para um Futuro Incerto

    Os insights obtidos não são apenas um reflexo do passado, mas também uma bússola para o futuro. Eles nos equipam para desenvolver políticas de saúde mais assertivas, especialmente em preparação para possíveis novos surtos.

    ### A Sinergia entre Dados e Ação

    Os dados da PNAD 2020 são um convite à ação. Eles nos desafiam a transformar análises em estratégias concretas, a utilizar a tecnologia como uma aliada e a promover a colaboração interdisciplinar como nunca antes.

    ### Avançando com Resiliência

    À medida que avançamos, levamos conosco as lições aprendidas e a determinação de aplicar esse conhecimento em prol de uma sociedade mais resiliente. Que as descobertas da PNAD 2020 inspirem e orientem o Brasil rumo a um futuro onde a saúde e o bem-estar são priorizados.

            
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