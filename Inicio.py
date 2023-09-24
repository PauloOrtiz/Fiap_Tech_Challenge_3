import streamlit as st
from PIL import Image

st.set_page_config(page_title="Início", page_icon=":house:")

image = Image.open("./src/img/inicio.jpg")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("""
# Navegando pelo Impacto da COVID-19: Uma Jornada pelos Dados

Em um mundo transformado por um inimigo invisível, a COVID-19, cada decisão, cada passo dado, tem o poder de moldar o nosso futuro. Mas, para tomar decisões acertadas, precisamos olhar para trás e entender o que aconteceu. E é exatamente isso que vamos fazer juntos nesta jornada.

---

A pandemia não afetou apenas a saúde das pessoas, mas também a maneira como vivemos, interagimos e até mesmo como a economia funciona. Para desvendar essa complexa teia de impactos, mergulhamos em uma das bases de dados mais ricas e confiáveis do Brasil: o PNAD-COVID-19 do IBGE.

---

## Nossa Missão:

Nossa expedição pelos dados nos levará por três trilhas principais:

1. **Trilha dos Sintomas Clínicos:** Aqui, exploraremos os sinais que a COVID-19 deixou em nosso corpo. Quais sintomas foram mais comuns? Existiram padrões ou anomalias que podemos identificar?
  
2. **Trilha do Comportamento da População:** Nesta trilha, entenderemos como nós, como sociedade, reagimos. Quais foram nossos medos, nossas ações e nossas esperanças durante os meses mais críticos da pandemia?
  
3. **Trilha Econômica:** A pandemia abalou as estruturas econômicas. Mas como? E quem foi mais afetado? Vamos desvendar os impactos econômicos que reverberaram por toda a sociedade.

---

## Nossos Limites:

Em nossa jornada, focaremos em 20 questionamentos cruciais e nos aprofundaremos em um período de 3 meses, garantindo que nossa análise seja tanto detalhada quanto relevante.

---

## Convite:

Convidamos você a se juntar a nós nesta exploração. Com os insights que descobrirmos, não apenas entenderemos melhor o que aconteceu, mas também estaremos mais preparados para o que pode vir pela frente.

---

*"O conhecimento é a bússola que nos guia em tempos de incerteza."*
""")


