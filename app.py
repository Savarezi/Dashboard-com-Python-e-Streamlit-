
import streamlit as st

# Dedinir titulo
st.title("Evento | Dashboard com Python e Streamlit")

# Cabeçalho
st.header("Conhecendo os elementos do Streamlit")

# subtitulo
st.subheader("Aula 2 [2/5]")

# Texto Simples
st.write("Nesta aula vamos entender os elementos do Streamlit")

# Texto formatado
st.markdown("# Streamlit")

# Texto
st.write("Streamlit é um framework de desenvolvimento de alto nível de python")

# Botão com validaçao
if st.button("Clique Aqui"):
    for loop in range(5):
      st.write(f"Botão Selecionado {loop}")

# Radio - selecionar uma opção
escolha = st.radio("Qual Linguagem de Programação vc mais ultiliza?", ("Python", "R", "Java", "C++", "C#" , " Outros"))
print(escolha)

# Selectbox
lsta_framework = ['Metiplolib', 'Flask', 'Django', 'Streamlit', 'Plotly' , 'Seaborn']
opcao = st.multiselect("Escolha um Framework", lsta_framework)


# Seleção múltipla
lista_estudos = ['Pandas', 'Numpy', 'Matplotlib', 'Seaborn', 'Plotly' , 'Streamlit']
opcao = st.multiselect("Escolha os Estudos", lista_estudos)

# Seleção de Valor

valor = st.slider("Qunatos anos Trabalha com Data Science", 0,30,1)

# Upload Files      

arquivo = st.file_uploader("Escolha um Arquivo", type=["csv", "txt"])

# Imagem
st.image('python.png',caption='Python é uma linguagem de programação versátil, fácil de aprender e amplamente usada em áreas como desenvolvimento web, automação, análise de dados e inteligência artificial.',use_column_width=True)



import pandas as pd 
import numpy as np
# Tabela
df = pd.DataFrame(
   {
      'Dias': [loop for loop in range(31)],
   }
)


# Adicinando no vas colunas com dados aleatórios
df["Valor de Venda"] = np.random.randint(100,1000,size=31)
df["Custo"] = df["Valor de Venda"]*0.8
df["Lucro"] = df["Valor de Venda"]-df["Custo"]
df["Qquantidade Vendida"]= np.random.randint(10,50,size=31)
df["Cliente"] = ["Cliente "+ str(i) for i in range(1,32)]

# Incluir essa tabela

st.dataframe(df)


import altair as alt

# Criar um Gráfico de Linhas com Altair

chart = alt.Chart(df).mark_line().encode(
    x='Dias',
    y='Lucro',
)
    

st.altair_chart(chart)

















