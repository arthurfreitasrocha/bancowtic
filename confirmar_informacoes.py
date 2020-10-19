from tratamento import tratarAlpha

import os

def telaConfirmarInformacoes(tipo_operacao, login, senha, **kws):

    '''
    EXIBE AS INFORMAÇÕES ESCRITAS PELO USUÁRIO
    E PEDE A CONFIRMAÇÃO DO MESMO
    '''

    if tipo_operacao == 'login':

        os.system('cls')

        print('\nDESEJA PROSSEGUIR COM AS INFORMAÇÕES ABAIXO? [S/N]\n')

        print(f'LOGIN: {login}')
        print(f'SENHA: {senha}\n')

        resp = input('>>> ')

        return_resp = tratarAlpha(resp)

        if return_resp == True:

            if resp == 's':
                return True


    elif tipo_operacao == 'cadastro':

        nome = kws.get('nome')
        idade = kws.get('idade')

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