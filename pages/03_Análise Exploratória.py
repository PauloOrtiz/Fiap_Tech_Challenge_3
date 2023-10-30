import streamlit as st
from PIL import Image

st.set_page_config(page_title="Análise Exploratória", page_icon=":house:")

image = Image.open("./src/img/Exploratoria.png")
imageSexo = Image.open("./src/img/Dash/Sociodemografica/Sexo.png")
imageIdade = Image.open("./src/img/Dash/Sociodemografica/idade.png")
imageDomicilio = Image.open("./src/img/Dash/Sociodemografica/Domicílio.png")
imagePlano = Image.open("./src/img/Dash/Sociodemografica/plano.png")
imageNvPlpositivo = Image.open("./src/img/Dash/Clinico/Tab_sintomas_maior_incidecia_para_caso_positivados.png")
imageNVPlentubado = Image.open("./src/img/Dash/Clinico/Tab_sintomas_internação.png")
imageBarraSistomas = Image.open("./src/img/Dash/Clinico/quant_positivo_negativo_por_sintoma.png")


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
        
        st.markdown("""
        # Análise Sociodemográfica: Entendendo o Impacto da Pandemia

        A pandemia da COVID-19 afetou diferentes segmentos da população de maneiras distintas. Ao explorar os aspectos sociodemográficos, buscamos entender como diferentes grupos foram impactados e quais padrões emergem desses dados.

        ## 1. Análise por Gênero

        Observando a divisão por gênero, **46,05%** dos entrevistados eram homens, dos quais **23,61%** testaram positivo para COVID-19. Por outro lado, **53,95%** eram mulheres, e surpreendentemente, **29,2%** delas testaram positivo. Esta diferença nos faz refletir sobre os comportamentos e exposições distintas entre os gêneros.
        """)

        st.image(imageSexo, caption='Distribuição por Gênero')

        st.markdown("""
        ## 2. Análise por Tipo de Domicílio

        Quando analisamos o tipo de domicílio, **86,91%** dos entrevistados residem em zonas urbanas, com **24,68%** deles testando positivo. Em contraste, **13,09%** vivem em zonas rurais, e **21,95%** destes testaram positivo. Estes números nos dão uma visão sobre a disseminação do vírus em diferentes ambientes e densidades populacionais.
        """)

        st.image(imageDomicilio, caption='Distribuição por Tipo de Domicílio')

        st.markdown("""
        ## 3. Análise por Faixa Etária

        A idade é um fator crucial na análise da COVID-19. **9,33%** dos entrevistados são menores de 18 anos, com **22%** testando positivo. A maior parte, **75,18%**, tem entre 19 e 59 anos, com **25,06%** positivos. Os idosos, representando **15,49%**, tiveram uma taxa de positividade de **22,02%**. Estes números nos ajudam a entender os grupos de risco e a necessidade de cuidados especiais para certas faixas etárias.
        """)

        st.image(imageIdade, caption='Distribuição por Faixa Etária')

        st.markdown("""
        ### Conclusão

        A análise sociodemográfica revelou padrões e tendências cruciais sobre o impacto da COVID-19 em diferentes segmentos da população. Estes insights são fundamentais para direcionar esforços, recursos e campanhas de conscientização. A pandemia nos mostrou a importância de entender as nuances da nossa sociedade, e com essas informações, estamos mais preparados para enfrentar desafios futuros e proteger os mais vulneráveis.
        """)

with tab3:
        st.markdown("""
        # Análise Clínica: Sintomas da COVID-19 e Seus Impactos

        A COVID-19, uma doença causada pelo novo coronavírus, apresentou uma variedade de sintomas nos pacientes, variando de leves a graves. A compreensão desses sintomas é crucial para identificar, tratar e, em última instância, controlar a propagação do vírus.

        Nesta seção, vamos mergulhar nos sintomas relatados pelos entrevistados e explorar como eles se correlacionam com os resultados dos testes e a gravidade da doença.

        ### Sintomas Mais Comuns em Pacientes Positivos

        Através de uma nuvem de palavras, podemos visualizar quais sintomas foram mais frequentemente relatados por aqueles que testaram positivo para a COVID-19.
        """)

        # Adicione o código para inserir a imagem da nuvem de palavras
        st.image(imageNvPlpositivo, caption="Nuvem de palavras dos sintomas em pacientes positivos.")

        st.markdown("""
        ## Relação entre Sintomas e Resultados de Testes

        A análise a seguir apresenta uma visão clara da relação entre os sintomas relatados e os resultados dos testes. Notavelmente, a perda de olfato (anosmia) mostrou uma forte correlação com testes positivos.
        """)

        # Adicione o código para inserir a imagem do gráfico de barras
        st.image(imageBarraSistomas, caption="Relação entre sintomas e resultados de testes.")

        st.markdown("""
        ## Sintomas em Pacientes Entubados

        A gravidade da COVID-19 em alguns pacientes levou à necessidade de entubação. A nuvem de palavras a seguir destaca os sintomas mais comuns relatados por pacientes que necessitaram de entubação.
        """)

        # Adicione o código para inserir a segunda imagem da nuvem de palavras
        st.image(imageNVPlentubado, caption="Nuvem de palavras dos sintomas em pacientes entubados.")

        st.markdown("""
        ### Conclusão

        A análise clínica nos oferece insights valiosos sobre a natureza da COVID-19 e seus efeitos nos pacientes. A identificação precoce de sintomas, especialmente aqueles fortemente correlacionados com testes positivos, é crucial para o tratamento oportuno e a prevenção da propagação. A necessidade de entubação em alguns pacientes reforça a gravidade potencial da doença e a importância de medidas preventivas e de controle. À medida que continuamos a enfrentar desafios relacionados à COVID-19, esses insights são fundamentais para informar estratégias de saúde pública e práticas clínicas.
        """)


with tab4:

        st.markdown("""
        # Análise Econômica: O Impacto da COVID-19 no Bolso dos Brasileiros

        A pandemia da COVID-19 não afetou apenas a saúde global, mas também teve repercussões significativas na economia. Muitos perderam empregos, enfrentaram cortes salariais e viram suas economias desaparecerem. No entanto, a realidade econômica de cada indivíduo é única e influenciada por diversos fatores.

        Nesta seção, exploraremos o aspecto econômico dos entrevistados, buscando entender como a pandemia afetou diferentes segmentos da população em termos financeiros. Vamos analisar a relação entre a posse de um plano de saúde e a capacidade de acesso a tratamentos, bem como outros indicadores econômicos que podem lançar luz sobre as desigualdades e desafios enfrentados durante este período turbulento.

        A economia e a saúde estão intrinsecamente ligadas, e entender essa relação é crucial para formular políticas e estratégias eficazes para o futuro.
        """)
        
        st.markdown("""
        ## 1. Análise de Plano de Saúde e Internações

        A disponibilidade de um plano de saúde pode influenciar o acesso ao tratamento. **28,24%** dos entrevistados possuem plano de saúde, e **12,5%** destes foram entubados. Em contraste, **71,76%** não possuem plano, e **22,95%** destes foram entubados. A maior taxa de entubação entre os que não têm plano pode refletir desafios no acesso a tratamentos precoces ou a cuidados de saúde de qualidade.
        """)

        st.image(imagePlano, caption='Distribuição por Plano de Saúde')

with tab5:
        pass