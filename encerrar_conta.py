from informacoes_usuario import capturarInformacoesUsuario
from diretorio_atual import capturarDiretorioUsuario

from validar_login import validarLogin
from tratamento import tratarAlpha, tratarOpcao
from sair import sairBanco

import os

def telaEncerrarConta():

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ENCERRAR CONTA]\n')

    print('PARA CONFIRMAR A EXCLUSÃO DE SUA CONTA DIGITE SEU LOGIN E SUA SENHA\n\
        OU DIGITE "sair" PARA SAIR.\n')

    login = input('LOGIN: ')

    if login.lower() == 'sair':
        return False

    senha = input('SENHA: ')

    if senha.lower() == 'sair':
        return False


    return_validacao = validarLogin(login, senha)
    print(return_validacao)

    if return_validacao == True:
        controleEncerrarConta(login)

    else:

        print('LOGIN E/OU SENHA INVÁLIDO(S)!\n')
        os.system('pause')

        return False


def controleEncerrarConta(login):

    informacoes_usuario = capturarInformacoesUsuario()

    nome = informacoes_usuario[0]

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ENCERRAR CONTA]\n')

    print(f'({nome}) TEM CERTEZA QUE VOCÊ DESEJA EXCLUIR SUA CONTA?\n\
        ESSA AÇÃO NÃO PODERÁ SER DESFEITA. [S/N]\n')

    resp = input('>>> ')

    return_resp = tratarAlpha(resp)


    if return_resp == True:

        return_resp = tratarOpcao(resp, 's', 'n')

        if return_resp == True:

            diretorio_usuario = capturarDiretorioUsuario(login)
            os.mkdir(diretorio_usuario)

            print('CONTA EXCLUÍDA COM SUCESSO.\n')
            os.system('pause')

            sairBanco()

