from tratamento import tratarNum, tratarOpcao

import os

def alterarInformacoesPessoais():

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ALTERAR INFORMAÇÕES PESSOAIS]\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) ALTERAR LOGIN')
    print('(02) ALTERAR SENHA\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False

    return_tratamento = tratarNum(resp)

    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:
            return resp


def controleAlterarInformacoesPessoais():

    pass