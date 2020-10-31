from .Tela_OperacoesBancarias import telaOperacoesBancarias
from .Tela_ConfiguracoesUsuario import telaConfiguracoesUsuario

from .InformacoesUsuario import capturarInformacoesUsuario
from .TratamentoErros import tratarNum, tratarOpcao
from .Tela_Sair import sairBanco

import os


def telaUsuario(login):

    informacoes_usuario = capturarInformacoesUsuario(login)

    nome = informacoes_usuario[0]

    os.system('cls')

    print(f'\nBANCO WTIC - [TELA USUÁRIO] - BEM-VINDO ({nome.title()})!\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) OPERAÇÕES BANCÁRIAS')
    print('(02) CONFIGURAÇÕES DO USUÁRIO\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        sairBanco()


    return_tratamento = tratarNum(resp)

    '''
    PARTE LÓGICA DA TELA USUÁRIO
    '''
    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:

            controleUsuario(resp, login)

    telaUsuario(login)


def controleUsuario(opcao, login):

    '''
    FUNÇÃO RESPONSÁVEL PELO CONTROLE DE FLUXO
    DAS TELAS DO USUÁRIO

    ====================================================

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 01
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA OPERAÇÕES BANCÁRIAS

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 02
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA CONFIGURAÇÕES DO USUÁRIO
    '''

    if opcao == 1:
        return_operacoes = telaOperacoesBancarias()

        if return_operacoes == False:
            telaUsuario(login)

    elif opcao == 2:
        return_configuracoes = telaConfiguracoesUsuario(login)

        if return_configuracoes[0] == False:
            login = return_configuracoes[1]
            telaUsuario(login)
