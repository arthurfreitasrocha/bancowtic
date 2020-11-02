from Usuario.ManipularArquivo import lerArquivo

import os

def telaExtrato(login):

    os.system('cls')

    print('\nBANCO WTIC - [OPERAÇÕES BANCÁRIAS -> EXTRATO]\n')

    print('===== SEU EXTRATO [INÍCIO] ====')

    endereco = f'Banco de Dados\\Usuarios\\{login}\\extrato.txt'
    extrato = lerArquivo(endereco)

    print(extrato)

    print('\n===== SEU EXTRATO [FIM] ====\n')

    os.system('pause')