from .TratamentoErros import tratarNum, tratarOpcao

import os

def telaOperacoesBancarias():

    os.system('cls')

    print('\nBANCO WTIC - [OPERAÇÕES BANCÁRIAS]\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) DEPÓSITO')
    print('(02) SAQUE')
    print('(03) TRANSFERÊNCIA')
    print('(04) EXTRATO\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False

    return_tratamento = tratarNum(resp)

    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2,3,4)

        if return_tratamento == True:
            return resp