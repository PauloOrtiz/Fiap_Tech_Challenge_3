import streamlit as st
from PIL import Image

st.set_page_config(page_title="Apache Spark", page_icon=":house:")

image = Image.open("./src/img/Apache.png")
st.image(image)

with open("./src/css/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.markdown("""
# Apache Spark: A Chave para Desvendar o Big Data

Em um mundo onde os dados são produzidos a uma velocidade vertiginosa, ferramentas poderosas são necessárias para decifrar, analisar e extrair valor deles. É aqui que entra o **Apache Spark**.

## O que é o Apache Spark?

O Apache Spark é uma plataforma de computação em cluster otimizada, projetada para ser rápida e de propósito geral. Ele permite que os desenvolvedores realizem análises de dados em grande escala, processando e analisando conjuntos de dados massivos de maneira eficiente e rápida. Com suas capacidades robustas, o Spark tornou-se uma ferramenta essencial para o processamento de Big Data.

## Por que escolhemos o Apache Spark?

Imagine tentar encher uma piscina olímpica com uma mangueira de jardim. Seria uma tarefa demorada e ineficiente. Da mesma forma, ao lidar com um banco de dados colossal de 950 mil registros, precisamos de uma "mangueira" mais potente. O Spark, com sua capacidade de processar dados em paralelo e sua integração perfeita com a AWS, nos permite analisar, transformar e extrair insights de nossos dados de maneira eficiente e eficaz.

## Bibliotecas-chave e suas funções:

- **Spark SQL**: Permite que trabalhemos com dados estruturados usando SQL, além de ser compatível com muitos formatos de dados, como JSON e Parquet.
- **Spark Streaming**: Processa fluxos de dados em tempo real, permitindo análises e ações imediatas.
- **MLlib**: Para aprendizado de máquina, nos permite aplicar algoritmos de aprendizado de máquina a grandes conjuntos de dados de maneira rápida.
- **GraphX**: Para análise de gráficos e computação, nos ajuda a entender as relações e padrões dentro de nossos dados.

""")