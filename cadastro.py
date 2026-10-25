import pandas as pd
import streamlit as st
import plotly.express as px
import openpyxl

# Passo 1: Criar a tela do sistema

st.write('# :blue[Cadastro de Produtos]')
tabela = pd.read_csv('bancodedados.csv' , low_memory=False)
tabela.columns = tabela.columns.str.strip()
tabela['Produto'] = tabela['Produto'].str.strip()
print(list(tabela.columns))
busca_produto = st.text_input('DIGITE O NOME DO PRODUTO QUE QUER ENCONTAR')
botao3 = st.button('BUSCAR')
# st.write('######  PRODUTOS DISPONÍVEIS')
tabela['Produto'] = tabela['Produto'].str.title()


if botao3:
    tabela['Produto'] = tabela['Produto'].str.title()
    tabela['Produto'] = tabela['Produto'].str.strip()
    tabela = tabela.sort_values(by='Produto')
    tabela = tabela.reset_index(drop=True)
    busca = tabela[(tabela['Produto'].str.contains(busca_produto, case=False, na=False, regex=False))]
    lista_de_busca = busca
    st.dataframe(busca) # Mostra a tabela

# Passo 2: Criar a aba lateral com os campos de cadastro

data = st.sidebar.date_input('Data')
produto = st.sidebar.text_input('Nome do Produto')
valor = st.sidebar.number_input('Valor (R$)')
fornecedor = st.sidebar.text_input('Fornecedor')
categoria = st.sidebar.selectbox('Categoria',['', 'Abertura', 'Casa', 'Chapa','Civil', 'Consumivel',
'Eletrica','EPI', 'Estetica Automotiva', 'Ferragem', 'Ferramenta', 'Fixacao', 'Hidraulica', 'Mecanica',
'Perfil', 'Servico'])
botao = st.sidebar.button('CADASTRAR')
# botao2 = st.sidebar.button('SALVAR.xlsx')

# Salvar os dados na planilha

if botao:
    novo_cadastro = [data, produto, valor, fornecedor, categoria]
    tabela.loc[len(tabela)] = novo_cadastro
    tabela.to_csv('bancodedados.csv', index=False)
    st.success('Cadastro Realizado Com Sucesso!')
    st.error("Produto Não Cadastrado Por Duplicidade")
    tabela['Produto'] = tabela['Produto'].str.strip()
    tabela = tabela.sort_values(by='Produto')
    tabela = tabela.reset_index(drop=True)
    tabela['Produto'] = tabela['Produto'].str.title()
    

# if botao2:
#     tabela.to_excel('Copia_de_Seguranca.xlsx',index=False)


    

# Mostrando a Base de dados

st.write('## :blue[Produtos Cadastrados]') # Título para tabela
st.dataframe(tabela) # Mostra a tabela

# Limpando a caixa de texto

# 1. Inicializa a variável no session_state se ela não existir

# if "texto_usuario" not in st.session_state:
#     st.session_state.texto_usuario = ""

# # 2. Função de callback que limpa o valor no session_state
# def limpar_texto():
#     st.session_state.texto_usuario = ""

# # 3. Cria o text_input vinculado à chave do session_state
# st.text_input("Buscador:", key="texto_usuario")

# # 4. Cria o botão que dispara a função de limpar
# st.button("Limpar Caixa de Texto", on_click=limpar_texto)

