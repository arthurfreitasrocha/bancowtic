from diretorio_atual import capturarDiretorioAtual
from confirmar_informacoes import telaConfirmarInformacoes
from validar_login import validarLogin

import os

def telaLogin():

    '''
    EXIBE A TELA DE LOGIN
    '''

    os.system('cls')

    print('\nBANCO WTIC - [LOGIN]\n')

    print('POR FAVOR INFORME OS DADOS ABAIXO OU DIGITE "sair" PARA SAIR\n')


    login = input('LOGIN: ')

    if login.lower() == 'sair':

        informacoes = [False, 0]
        return informacoes

    senha = input('SENHA: ')

    if senha.lower() == 'sair':

        informacoes = [False, 0]
        return informacoes


    return_confirmar = telaConfirmarInformacoes('login', login, senha)

    if return_confirmar == True:

        diretorio_atual = capturarDiretorioAtual()
        diretorio_usuarios = f'{diretorio_atual}\\usuarios'

        usuarios = os.listdir(diretorio_usuarios)

        if usuarios == []:
            print('\nUSUÁRIO OU SENHA INVÁLIDOS\n')
            os.system('pause')

            telaLogin()

        else:

            return_validacao = validarLogin(login, senha)

            if return_validacao == True:

                print('\nLOGADO COM SUCESSO!\n')
                os.system('pause')

                informacoes = [True, login]

                return informacoes

            else:
                print('\nFALHA NO LOGIN\n')
                os.system('pause')

                telaLogin()

    else:
        telaLogin()
