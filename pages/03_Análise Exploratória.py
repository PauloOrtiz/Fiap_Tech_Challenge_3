import streamlit as st
from PIL import Image

st.set_page_config(page_title="Análise Exploratória", page_icon=":house:")

image = Image.open("./src/img/Exploratoria.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Introdução","Sociodemográfico","Clínico","Econômico", "Perfil geral da população"])

with tab1:

        
        st.markdown("""
        # Análise Exploratória: Uma Jornada pelos Impactos da Pandemia

        Durante três intensos meses, o mundo enfrentou mais do que uma crise de saúde. A COVID-19 revelou-se uma tempestade perfeita, afetando todos os aspectos de nossa sociedade: desde a saúde até a economia, passando pelas relações sociais e padrões de comportamento.

        Neste cenário, cada dado, cada número, conta uma história. E é nossa missão, através desta análise exploratória, dar voz a essas histórias silenciosas, mas profundamente reveladoras. Vamos nos aprofundar nas camadas da sociedade, entender os desafios enfrentados por diferentes grupos e descobrir as nuances ocultas por trás dos números brutos.

        ## Nossos Temas de Exploração:

        ### Sociodemográfico:
        Aqui, exploraremos como diferentes segmentos da população foram afetados. Como a pandemia influenciou diferentes faixas etárias, gêneros e grupos socioeconômicos? Quais foram os padrões de comportamento adotados e como eles se refletiram na propagação do vírus?

        ### Clínico:
        A saúde é, obviamente, o epicentro desta crise. Mas quais sintomas foram mais comuns? Existem correlações entre certos sintomas e a gravidade da doença? Como o acesso a serviços de saúde influenciou os resultados para os pacientes?

        ### Econômico:
        A economia foi profundamente afetada pela pandemia. Mas como exatamente? Quais grupos foram mais vulneráveis? Como os padrões de trabalho mudaram e quais foram as implicações econômicas de longo prazo?

        
        """)
        
with tab2:
        pass

with tab3:
        pass

with tab4:
        pass

with tab5:
        pass