from Usuario.TratamentoErros import tratarNum
from Usuario.ManipularArquivo import escreverArquivo, lerArquivo, acrescentarTextoArquivo

import os

def telaDeposito(login):

    os.system('cls')

    print('\nBANCO WTIC - [OPERAÇÕES BANCÁRIAS -> DEPÓSITO]\n')

    print('POR FAVOR INFORME O VALOR A SER DEPOSITADO OU DIGITE "sair" PARA SAIR\n')

    valor = input('R$ ')

    if valor.lower() == 'sair':
        return False

    return_tratamento = tratarNum(valor)

    if return_tratamento == True:

        saldo_atual = controleDeposito(valor, login)

        print(f'\nDEPÓSITO REALIZADO COM SUCESSO! SEU SALDO ATUAL É: R$ {saldo_atual}\n')
        os.system('pause')

        return True

    telaDeposito(login)


def controleDeposito(valor, login):

    '''
    FAZ O DEPÓSITO
    '''

    valor = float(valor)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    saldo = float(lerArquivo(endereco))

    saldo += valor
    saldo = str(saldo)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    escreverArquivo(endereco, saldo)


    '''
    ESCREVE O RELATÓRIO DO DEPÓSITO NO EXTRATO
    '''

    endereco = f'Banco de Dados\\Usuarios\\{login}\\extrato.txt'
    relatorio = f'\nDEPÓSITO DE R$ {valor} REALIZADO COM SUCESSO! SALDO ATUAL: R$ {saldo}'
    acrescentarTextoArquivo(endereco, relatorio)

    return saldo