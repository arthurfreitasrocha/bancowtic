import os

def capturarInformacoesUsuario(login):

    '''
    ESSA FUNÇÃO É RESPONSÁVEL POR CAPTURAR
    AS INFORMAÇÕES PESSOAIS DO USUÁRIO (NOME, IDADE)
    '''

    diretorio_usuario = f'Banco de Dados\\Usuarios\\{login}'

    nome_arquivos = ['nome.txt', 'idade.txt']
    informacoes_usuario = []

    for nome_arquivo in nome_arquivos:

        diretorio_arquivo = f'{diretorio_usuario}\\{nome_arquivo}' # 'C:\Users\arthu\Documents\GitHub\bancowtic\usuarios\123\nome.txt'

        arquivo = open(diretorio_arquivo, 'r')
        informacao = arquivo.read()
        arquivo.close()

        informacoes_usuario.append(informacao)

    return informacoes_usuario