import pyautogui as pa
import pandas as pd
import time
import openpyxl

pa.PAUSE = 1

tabela = pd.read_excel('bancodedados.xlsx')
# print(tabela)



for linha in tabela.index:
    pa.moveTo(x=1494, y=287, duration=0.3)
    pa.click(x=1494, y=287)
    pa.write(str(tabela.loc[linha, 'Produto']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'Valor']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'Fornecedor']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'Categoria']))
    pa.press('enter')
    pa.press('tab')
    pa.press('enter')

