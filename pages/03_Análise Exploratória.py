import streamlit as st
from PIL import Image

st.set_page_config(page_title="Análise Exploratória", page_icon=":house:")

image = Image.open("./src/img/Exploratoria.jpg")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1 = st.tabs(["Introdução"])

with tab1:

        st.markdown("""
                ## Análise Exploratória: Desvendando os Mistérios da Pandemia

                Em um período de três meses, o mundo foi sacudido por uma onda de incertezas, medos e desafios. A COVID-19 não foi apenas uma crise de saúde, mas também uma crise social e econômica. Para prever e se preparar para futuras pandemias, precisamos entender profundamente o que aconteceu durante esse período crucial.

                Nossa missão aqui é clara: **analisar o contexto social, econômico e clínico** para identificar padrões, tendências e insights. Com base nas perguntas que selecionamos na página de dados, vamos nos aprofundar em diversas análises que nos ajudarão a entender melhor o impacto da pandemia em diferentes segmentos da população.

                ### Análises a serem realizadas:

                #### Sociodemográfico:
                - % população positivada por UF
                - % população positivada por UF analise rural/urbana
                - % positivado por gênero
                - Agregar todos que disseram que tiveram algum sintoma e cruzar com nível de isolamento
                - Nível de isolamento social entre faixa etária
                - Nível de isolamento por renda
                - Nível de isolamento social entre quem te plano de saúde e não
                - Internação por idade
                - Uso de respirador por idade
                - Auxilio emergencial por cor
                - Home office por renda

                #### Clínico:
                - Análise sintoma com positivados, agregar todos que responderam sim a alguma pergunta de sintoma para cruzar com positivados
                - Cruzamento dos sintomas com internação
                - Cruzamento dos sintomas com necessidade respirador
                - Cruzar internação com se tem plano de saúde ou não
                - Cruzar necessidade de respirador com tem plano de saúde ou não

                #### Econômico:
                - Plano de saúde ou não por faixa de renda
                - Internação por faixa de renda
                - Uso de respirador por renda

                ---

                **Convite:**  
                Convido você a se juntar a mim nesta exploração. A cada análise, revelaremos uma peça do quebra-cabeça, aproximando-nos de uma compreensão mais clara do impacto da pandemia. Juntos, vamos transformar dados brutos em conhecimento e preparar-nos melhor para o futuro.

                **Vamos começar?**
                """)