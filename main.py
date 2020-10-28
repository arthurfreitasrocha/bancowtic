from Tela_Inicio import telaInicio

import os

'''
VERIFICA SE A PASTA "usuarios" JA FOI CRIADA
'''

arquivos_no_diretorio = os.listdir('Banco de Dados')

if arquivos_no_diretorio == []:
    os.mkdir('Banco de Dados\\Usuarios')


telaInicio()
