from Usuario.TratamentoErros import tratarAlpha

import os

def telaConfirmarInformacoes(nome, idade, login, senha):

    '''
    EXIBE AS INFORMAÇÕES ESCRITAS PELO USUÁRIO
    E PEDE A CONFIRMAÇÃO DO MESMO
    '''

    os.system('cls')

    print('\nDESEJA PROSSEGUIR COM AS INFORMAÇÕES ABAIXO? [S/N]\n')

    print(f'NOME: {nome}')
    print(f'IDADE: {idade}')
    print(f'LOGIN: {login}')
    print(f'SENHA: {senha}\n')

    resp = input('>>> ')

    return_resp = tratarAlpha(resp)

    if return_resp == True:

        if resp == 's':
            return True

        return False