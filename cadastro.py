import pandas as pd
import streamlit as st
import plotly.express as px




# Passo 1: Criar a tela do sistema

st.write('# :blue[Cadastro de Produtos]')
tabela = pd.read_csv('bancodedados.csv')
# Passo 2: Criar a aba lateral com os campos de cadastro

data = st.sidebar.date_input('Data')
produto = st.sidebar.text_input('Nome do Produto')
valor = st.sidebar.number_input('Valor (R$)')
fornecedor = st.sidebar.text_input('Fornecedor')
categoria = st.sidebar.selectbox('Categoria',['', 'Abertura', 'Casa', 'Chapa','Civil', 'Consumível',
'Elétrica','EPI', 'Estética Automotiva', 'Ferragem', 'Ferramenta', 'Fixação', 'Hidraulica', 'Mecânica',
'Perfil', 'Serviço'])
botao = st.sidebar.button('Salvar')


# Salvar os dados na planilha

if botao:
    novo_cadastro = [data, produto, valor, fornecedor, categoria]
    tabela.loc[len(tabela)] = novo_cadastro
    tabela.to_csv('bancodedados.csv', index=False)
    st.success('Cadastro Realizado Com Sucesso!')


    

# Mostrando a Base de dados

st.write('## :blue[Produtos Cadastrados]') # Título para tabela
st.dataframe(tabela) # Mostra a tabela



