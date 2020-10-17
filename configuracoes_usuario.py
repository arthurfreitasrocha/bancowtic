from tratamento import tratarNum, tratarOpcao

import os

def telaConfiguracoesUsuario():

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO]\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) ALTERAR INFORMAÇÕES PESSOAIS')
    print('(02) ENCERRAR CONTA\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False

    return_tratamento = tratarNum(resp)

    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:
            return resp