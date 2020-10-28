import os

def capturarDiretorioUsuario(login):

    '''
    CAPTURA O DIRETÓRIO DO USUÁRIO
    '''

    diretorio_atual = os.path.dirname(os.path.realpath(__file__))
    diretorio_usuario = f'{diretorio_atual}\\usuarios\\{login}'

    return diretorio_usuario


def capturarInformacoesUsuario(login):

    '''
    ESSA FUNÇÃO É RESPONSÁVEL POR CAPTURAR
    AS INFORMAÇÕES PESSOAIS DO USUÁRIO (NOME, IDADE)
    '''

    diretorio_usuario = capturarDiretorioUsuario(login)

    nome_arquivos = ['nome.txt', 'idade.txt']
    informacoes_usuario = []

    for nome_arquivo in nome_arquivos:

        diretorio_arquivo = f'{diretorio_usuario}\\{nome_arquivo}' # 'C:\Users\arthu\Documents\GitHub\bancowtic\usuarios\123\nome.txt'

        arquivo = open(diretorio_arquivo, 'r')
        informacao = arquivo.read()
        arquivo.close()

        informacoes_usuario.append(informacao)

    return informacoes_usuario