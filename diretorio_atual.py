import os

def capturarDiretorioAtual():

    '''
    CAPTURA O DIRETÓRIO QUE O CÓDIGO ESTÁ SENDO RODADO
    '''

    diretorio_atual = os.path.dirname(os.path.realpath(__file__))

    return diretorio_atual


def capturarDiretorioUsuario(login):

    '''
    CAPTURA O DIRETÓRIO DO USUÁRIO
    '''

    diretorio_usuario = f'usuarios\\{login}'

    return diretorio_usuario