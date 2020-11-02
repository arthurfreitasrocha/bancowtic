from Tela_ValidarLogin import telaValidarLogin
from Usuario.TratamentoErros import tratarNum, tratarOpcao

import os

def telaAlterarInformacoesPessoais(login):

    '''
    EXIBE A TELA PARA ALTERAR AS INFORMAÇÕES PESSOAIS
    '''

    return_validacao = telaValidarLogin()

    if return_validacao == False:
        return False


    os.system('cls')

    print('\nBANCO WTIC - [TELA USUÁRIO -> CONFIGURAÇÕES DO USUÁRIO -> ALTERAR INFORMAÇÕES PESSOAIS]\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) ALTERAR LOGIN')
    print('(02) ALTERAR SENHA\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False


    return_alterar_informacoes = controleAlterarInformacoesPessoais(resp, login)

    if return_alterar_informacoes == False:
        return False


def controleAlterarInformacoesPessoais(resp, login):

    '''
    FUNÇÃO RESPONSÁVEL PELO CONTROLE DE FLUXO
    DA OPÇÃO ESCOLHIDA PELO USUÁRIO

    ====================================================

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 01
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA ALTERAR LOGIN

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 02
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA ALTERAR SENHA
    '''

    return_tratamento = tratarNum(resp)

    if return_tratamento == True:


        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:


            if resp == 1:
                return_login = mudarLogin(login)

                if return_login == False:
                    return False

                return return_login

            elif resp == 2:
                return_senha = mudarSenha(login)

                if return_senha == False:
                    return False


def mudarLogin(login):

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ALTERAR INFORMAÇÕES PESSOAIS -> ALTERAR LOGIN]\n')

    print('POR FAVOR INFORME SEU [NOVO] LOGIN OU DIGITE "sair" PARA SAIR\n')

    novo_login = input('>>> ')

    if novo_login.lower() == 'sair':
        return False


    '''
    RENOMEIA A PASTA E EM SEGUIDA REESCREVE O ARQUIVO LOGIN
    A RENOMEAÇÃO DA PASTA É NECESSÁRIA PORQUE
    O NOME DA MESMA É O LOGIN DO USUÁRIO
    '''

    pasta_antiga = f'Banco de Dados\\Usuarios\\{login}'
    pasta_nova = f'Banco de Dados\\Usuarios\\{novo_login}'

    os.rename(pasta_antiga, pasta_nova)


    arquivo_login = f'{pasta_nova}\\login.txt'

    arquivo = open(arquivo_login, 'w')
    arquivo.write(novo_login)
    arquivo.close()


    print('\nLOGIN ALTERADO COM SUCESSO!\n')
    os.system('pause')

    return novo_login


def mudarSenha(login):

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ALTERAR INFORMAÇÕES PESSOAIS -> ALTERAR SENHA]\n')

    print('POR FAVOR INFORME SUA [NOVA] SENHA OU DIGITE "sair" PARA SAIR\n')

    nova_senha = input('>>> ')

    if nova_senha.lower() == 'sair':
        return False


    '''
    ALTERA A SENHA DO USUÁRIO
    '''
    arquivo_senha = f'Banco de Dados\\Usuarios\\{login}\\senha.txt'

    arquivo = open(arquivo_senha, 'w')
    arquivo.write(nova_senha)
    arquivo.close()


    print('\nSENHA ALTERADA COM SUCESSO!\n')
    os.system('pause')