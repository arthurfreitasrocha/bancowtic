from login import telaLogin
from cadastro import telaCadastro

from usuario import telaUsuario

from tratamento import tratarNum, tratarOpcao
from sair import sairBanco

import os

def telaInicio():

    '''
    EXIBE A TELA INICIAL DE LOGIN OU CADASTRO
    '''

    os.system('cls')

    print('\nBEM-VINDO AO BANCO WTIC!\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR:\n')

    print('(01) LOGIN')
    print('(02) CADASTRO\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        sairBanco()

    return_tratamento = tratarNum(resp)


    '''
    PARTE LÓGICA DA TELA INÍCIO
    '''
    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:

            controleInicio(resp)


    telaInicio()


def controleInicio(resp):

    '''
    FUNÇÃO RESPONSÁVEL PELO CONTROLE DE FLUXO
    DAS TELAS INICIAS, LOGIN E CADASTRO

    ====================================================

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 01
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA DE LOGIN

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 02
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA DE CADASTRO
    '''

    if resp == 1:

        return_login = telaLogin()

        if return_login[0] == True:

            login = return_login[1]
            telaUsuario(login)

        elif return_login == False:
            telaInicio()


    elif resp == 2:

        return_cadastro = telaCadastro()

        if return_cadastro == True:
            controleInicio(1)

        telaInicio()
