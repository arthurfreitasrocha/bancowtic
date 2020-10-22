from informacoes_usuario import capturarInformacoesUsuario
from diretorio_atual import capturarDiretorioUsuario

from validar_login import validarLogin
from tratamento import tratarAlpha, tratarOpcao
from sair import sairBanco

import os

def telaEncerrarConta():

    os.system('cls')

    print('\nBANCO WTIC - [TELA USUÁRIO -> CONFIGURAÇÕES DO USUÁRIO -> ENCERRAR CONTA]\n')

    print('PARA CONFIRMAR A EXCLUSÃO DE SUA CONTA DIGITE SEU LOGIN E SUA SENHA\n\
        OU DIGITE "sair" PARA SAIR.\n')

    login = input('LOGIN: ')

    if login.lower() == 'sair':
        return False

    senha = input('SENHA: ')

    if senha.lower() == 'sair':
        return False


    return_validacao = validarLogin(login, senha)

    if return_validacao == True:
        controleEncerrarConta(login)

    else:

        print('\nLOGIN E/OU SENHA INVÁLIDO(S)!\n')
        os.system('pause')

        return False


def controleEncerrarConta(login):

    informacoes_usuario = capturarInformacoesUsuario(login)

    nome = informacoes_usuario[0]

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ENCERRAR CONTA]\n')

    print(f'({nome.title()}) TEM CERTEZA QUE VOCÊ DESEJA EXCLUIR SUA CONTA?\n\
        ESSA AÇÃO NÃO PODERÁ SER DESFEITA. [S/N]\n')

    resp = input('>>> ')

    return_resp = tratarAlpha(resp)


    if return_resp == True:

        return_resp = tratarOpcao(resp, 's', 'n')

        if return_resp == True:

            if resp == 's':

                diretorio_usuario = capturarDiretorioUsuario(login)

                '''
                APAGA OS ARQUIVOS DENTRO DA PASTA DO USUÁRIO
                E EM SEGUIDA, APAGA SUA PASTA
                '''
                nome_arquivos = ['extrato.txt', 'idade.txt', 'login.txt', 'nome.txt', 'saldo.txt', 'senha.txt']

                for nome_arquivo in nome_arquivos:

                    arquivo = f'{diretorio_usuario}\\{nome_arquivo}'
                    os.remove(arquivo)

                os.removedirs(diretorio_usuario)

                print('\nCONTA EXCLUÍDA COM SUCESSO.')

                sairBanco()


            elif resp == 'n':

                print('\nOPERAÇÃO CANCELADA\n')
                os.system('pause')

                return False

