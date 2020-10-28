from diretorio_atual import capturarDiretorioAtual, capturarDiretorioUsuario
from validar_login import validarLogin
from tratamento import tratarNum, tratarOpcao

import os

def telaAlterarInformacoesPessoais(login):

    return_validacao = validarLogin()

    if return_validacao == True:
        return_controle = controleAlterarInformacoesPessoais(login)

        return return_controle

    else:
        return False


def controleAlterarInformacoesPessoais(login):

    os.system('cls')

    print('\nBANCO WTIC - [TELA USUÁRIO -> CONFIGURAÇÕES DO USUÁRIO -> ALTERAR INFORMAÇÕES PESSOAIS]\n')

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

            if resp == 1:
                return_login = mudarLogin(login)

                if return_login == False:
                    controleAlterarInformacoesPessoais(login)

                return True

            elif resp == 2:
                return_senha = mudarSenha(login)

                if return_senha == False:
                    controleAlterarInformacoesPessoais(login)

                return True


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

    pasta_antiga = capturarDiretorioUsuario(login)

    nova_pasta = capturarDiretorioAtual()
    nova_pasta = f'{nova_pasta}\\usuarios\\{novo_login}'

    os.rename(pasta_antiga, nova_pasta)


    arquivo_login = f'{nova_pasta}\\login.txt'

    arquivo = open(arquivo_login, 'w')
    arquivo.write(novo_login)
    arquivo.close()


    print('\nLOGIN ALTERADO COM SUCESSO!\n')
    os.system('pause')

    return True


def mudarSenha(login):

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ALTERAR INFORMAÇÕES PESSOAIS -> ALTERAR SENHA]\n')

    print('POR FAVOR INFORME SUA [NOVA] SENHA OU DIGITE "sair" PARA SAIR\n')

    nova_senha = input('>>> ')

    if nova_senha.lower() == 'sair':
        return False


    '''
    CAPTURA O ENDEREÇO DA PASTA DO USUÁRIO
    '''
    pasta_usuario = capturarDiretorioUsuario(login)


    '''
    ALTERA A SENHA DO USUÁRIO
    '''
    arquivo_senha = f'{pasta_usuario}\\senha.txt'

    arquivo = open(arquivo_senha, 'w')
    arquivo.write(nova_senha)
    arquivo.close()


    print('\nSENHA ALTERADA COM SUCESSO!\n')
    os.system('pause')

    return True