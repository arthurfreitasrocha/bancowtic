from Usuario.InformacoesUsuario import capturarInformacoesUsuario

from Tela_ValidarLogin import telaValidarLogin
from Usuario.TratamentoErros import tratarAlpha, tratarOpcao
from Usuario.Tela_Sair import sairBanco

import os

def telaEncerrarConta(login):

    '''
    EXIBE A TELA PARA ENCERRAR A CONTA
    '''

    os.system('cls')

    return_validacao = telaValidarLogin()

    if return_validacao == False:
        return False


    informacoes_usuario = capturarInformacoesUsuario(login)

    nome = informacoes_usuario[0]

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO -> ENCERRAR CONTA]\n')

    print(f'({nome.title()}) TEM CERTEZA QUE VOCÊ DESEJA EXCLUIR SUA CONTA?\n\
        ESSA AÇÃO NÃO PODERÁ SER DESFEITA. [S/N]\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False

    print(resp, login)
    controleEncerrarConta(resp, login)

    return False


def controleEncerrarConta(resp, login):

    '''
    FUNÇÃO RESPONSÁVEL POR EXCLUIR A CONTA DO USUÁRIO
    '''

    return_resp = tratarAlpha(resp)

    if return_resp == True:


        return_resp = tratarOpcao(resp, 's', 'n')

        if return_resp == True:

            '''
            APAGA A CONTA DO USUÁRIO SE resp == 's'
            '''
            if resp == 's':

                diretorio_usuario = f'Banco de Dados\\Usuarios\\{login}'

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

