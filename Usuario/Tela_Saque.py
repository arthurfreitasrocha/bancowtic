from Usuario.TratamentoErros import tratarNum
from Usuario.ManipularArquivo import escreverArquivo, lerArquivo, acrescentarTextoArquivo

import os

def telaSaque(login):

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    saldo = lerArquivo(endereco)

    os.system('cls')

    print(f'\nBANCO WTIC - [OPERAÇÕES BANCÁRIAS -> SAQUE] - SALDO ATUAL: (R$ {saldo})\n')

    print('POR FAVOR INFORME O VALOR A SER SACADO OU DIGITE "sair" PARA SAIR\n')

    valor = input('R$ ')

    if valor.lower() == 'sair':
        return False

    return_tratamento = tratarNum(valor)

    if return_tratamento == True:

        return_saque = controleSaque(valor, login)

        if return_saque == False:
            print('\nFALHA NO SAQUE. VOCÊ NÃO POSSUI SALDO SUFICIENTE\n')
            os.system('pause')

        else:

            saldo_atual = return_saque

            print(f'\nSAQUE REALIZADO COM SUCESSO! SEU SALDO ATUAL É: R$ {saldo_atual}\n')
            os.system('pause')

        return True

    telaSaque(login)


def controleSaque(valor, login):

    valor = float(valor)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    saldo = float(lerArquivo(endereco))

    temp = saldo - valor

    if temp < 0:
        return False

    saldo = str(temp)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    escreverArquivo(endereco, saldo)


    '''
    ESCREVE O RELATÓRIO DO DEPÓSITO NO EXTRATO
    '''

    endereco = f'Banco de Dados\\Usuarios\\{login}\\extrato.txt'
    relatorio = f'\nSAQUE DE R$ {valor} REALIZADO COM SUCESSO! SALDO ATUAL: R$ {saldo}'
    acrescentarTextoArquivo(endereco, relatorio)

    return saldo