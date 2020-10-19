from diretorio_atual import capturarDiretorioAtual
from confirmar_informacoes import telaConfirmarInformacoes

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
                print(login)

                informacoes = [True, login]

                return informacoes

            else:
                print('\nFALHA NO LOGIN\n')
                os.system('pause')

                telaLogin()

    else:
        telaLogin()


def validarLogin(login, senha):

    '''
    FAZ A VALIDAÇÃO DO LOGIN
    '''

    diretorio_atual = capturarDiretorioAtual()
    diretorio_usuarios = f'{diretorio_atual}\\usuarios'

    usuarios = os.listdir(diretorio_usuarios)


    usuario_existente = False
    for usuario in usuarios:

        if usuario == login:
            usuario_existente = True


    if usuario_existente == True:

        endereco_login = f'{diretorio_usuarios}\\{login}\\login.txt'
        endereco_senha = f'{diretorio_usuarios}\\{login}\\senha.txt'
        
        arquivo = open(endereco_login, 'r')
        login_arquivo = arquivo.read()
        arquivo.close()

        arquivo = open(endereco_senha, 'r')
        senha_arquivo = arquivo.read()
        arquivo.close()


        '''
        SE O LOGIN INFORMADO NÃO COINCIDIR COM OS DADOS NO
        BANCO DE DADOS OCORRERÁ A FALHA NO LOGIN
        '''
        if login_arquivo == login and senha_arquivo == senha:
            return True
        
        else:
            return False

    else:
        return False
