from Usuario.Tela_Deposito import telaDeposito
from Usuario.Tela_Saque import telaSaque
from Usuario.Tela_Transferencias import telaTransferencias
from Usuario.Tela_Extrato import telaExtrato
from Usuario.TratamentoErros import tratarNum, tratarOpcao

from Usuario.ManipularArquivo import lerArquivo

import os

def telaOperacoesBancarias(login):

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    saldo = lerArquivo(endereco)

    os.system('cls')

    print(f'\nBANCO WTIC - [OPERAÇÕES BANCÁRIAS] - SALDO ATUAL: (R$ {saldo})\n')

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

            controleOperacoesBancarias(resp, login)


def controleOperacoesBancarias(opcao, login):

    '''
    FUNÇÃO RESPONSÁVEL PELO CONTROLE DE FLUXO
    DAS TELAS OPERAÇÕES BANCÁRIAS

    ====================================================

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 01
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA DEPÓSITO

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 02
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA SAQUE

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 03
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA TRANSFERÊNCIAS

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 04
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA EXTRATO
    '''

    if opcao == 1:
        telaDeposito(login)

        telaOperacoesBancarias(login)

    elif opcao == 2:
        telaSaque(login)

        telaOperacoesBancarias(login)

    elif opcao == 3:
        telaTransferencias(login)

        telaOperacoesBancarias(login)

    elif opcao == 4:
        telaExtrato(login)

        telaOperacoesBancarias(login)