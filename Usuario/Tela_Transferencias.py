from Usuario.TratamentoErros import tratarNum
from Usuario.ManipularArquivo import lerArquivo, escreverArquivo, acrescentarTextoArquivo

import os

def telaTransferencias(login):

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    saldo = lerArquivo(endereco)

    os.system('cls')

    print(f'\nBANCO WTIC - [OPERAÇÕES BANCÁRIAS -> TRANSFERÊNCIA] - SALDO ATUAL: (R$ {saldo})\n')

    print('POR FAVOR INFORME A CONTA QUE RECEBERÁ A TRANSFERÊNCIA OU DIGITE "sair" PARA SAIR\n')

    conta_destino = input('>>> ')

    if conta_destino.lower() == 'sair':
        return False

    return_tratamento = tratarNum(conta_destino)

    nome_destino = ''
    if return_tratamento == True:

        return_existir_conta = verificarExistenciaConta(conta_destino)

        if return_existir_conta == False or conta_destino == login:

            print('\nCONTA INVÁLIDA OU INEXISTENTE!\n')
            os.system('pause')

            telaTransferencias(login)

        nome_destino = return_existir_conta


    print(f'\n\nPOR FAVOR INFORME O VALOR QUE SERÁ TRANSFERIDO PARA ({nome_destino.title()}) OU DIGITE "sair" PARA SAIR\n')

    valor = input('R$ ')

    if valor.lower() == 'sair':
        return False

    return_tratamento = tratarNum(valor)

    if return_tratamento == True:

        valor = int(valor)

        if valor < 0:

            print('\nVALOR INVÁLIDO!\n')
            os.system('pause')

            telaTransferencias(login)

        return_transferencia = controleTransferencias(conta_destino, login, valor)

        if return_transferencia == False:

            print('\nSALDO INSUFICIENTE PARA REALIZAR A TRANSFERÊNCIA!\n')
            os.system('pause')

            telaTransferencias(login)

        nome_destino = return_transferencia[0]
        nome_origem = return_transferencia[1]
        saldo_atual = return_transferencia[2]

        print(f'\n\nTRANSFERÊNCIA DE {nome_origem.title()} PARA {nome_destino.title()} REALIZADA COM SUCESSO! SEU SALDO ATUAL É: R$ {saldo_atual}\n')
        os.system('pause')

        return True


def verificarExistenciaConta(conta_destino):

    '''
    VERIFICA SE A CONTA DESTINO EXISTE
    '''

    lista_usuarios = os.listdir('Banco de Dados\\Usuarios')

    for usuario in lista_usuarios:

        if conta_destino == usuario:
            
            endereco = f'Banco de Dados\\Usuarios\\{conta_destino}\\nome.txt'
            nome_destino = lerArquivo(endereco)

            return nome_destino

    return False


def controleTransferencias(conta_destino, login, valor):

    '''
    CAPTURA DADOS DA CONTA DESTINO
    '''

    endereco = f'Banco de Dados\\Usuarios\\{conta_destino}\\nome.txt'
    nome_destino = lerArquivo(endereco)

    endereco = f'Banco de Dados\\Usuarios\\{conta_destino}\\saldo.txt'
    saldo_destino = lerArquivo(endereco)


    '''
    CAPTURA DADOS DA CONTA DESTINO
    '''

    endereco = f'Banco de Dados\\Usuarios\\{login}\\nome.txt'
    nome_origem = lerArquivo(endereco)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    saldo_origem = lerArquivo(endereco)


    '''
    REALIZA A TRANSFERÊNCIA
    '''

    saldo_destino = float(saldo_destino)
    saldo_origem = float(saldo_origem)
    valor = float(valor)


    if saldo_origem < valor:
        return False

    saldo_destino += valor
    saldo_origem -= valor


    '''
    ESCREVE NOS ARQUIVOS A TRANSFERÊNCIA
    '''

    saldo_destino = str(saldo_destino)
    saldo_origem = str(saldo_origem)

    endereco = f'Banco de Dados\\Usuarios\\{conta_destino}\\saldo.txt'
    escreverArquivo(endereco, saldo_destino)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\saldo.txt'
    escreverArquivo(endereco, saldo_origem)


    '''
    ESCREVE NOS EXTRATOS AS ALTERAÇÕES
    '''

    endereco = f'Banco de Dados\\Usuarios\\{conta_destino}\\extrato.txt'
    relatorio = f'\nTRANSFERÊNCIA RECEBIDA DE {nome_origem.title()} NO VALOR DE: R$ {valor}'
    acrescentarTextoArquivo(endereco, relatorio)

    endereco = f'Banco de Dados\\Usuarios\\{login}\\extrato.txt'
    relatorio = f'\nTRANSFERÊNCIA ENVIADA PARA {nome_destino.title()} NO VALOR DE: R$ {valor}'
    acrescentarTextoArquivo(endereco, relatorio)


    '''
    RETORNA ALGUMAS INFORMAÇÕES NECESSÁRIAS
    '''

    informacoes = [nome_destino, nome_origem, saldo_origem]
    return informacoes