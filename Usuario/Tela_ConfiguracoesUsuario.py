from encerrar_conta import telaEncerrarConta
from tratamento import tratarNum, tratarOpcao
from alterar_informacoes_pessoais import telaAlterarInformacoesPessoais

import os

def telaConfiguracoesUsuario(login):

    os.system('cls')

    print('\nBANCO WTIC - [TELA USUÁRIO -> CONFIGURAÇÕES DO USUÁRIO]\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) ALTERAR INFORMAÇÕES PESSOAIS')
    print('(02) ENCERRAR CONTA\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False

    return_tratamento = tratarNum(resp)

    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:
            controleConfiguracoesUsuario(resp, login)

    telaConfiguracoesUsuario(login)


def controleConfiguracoesUsuario(opcao, login):

    '''
    FUNÇÃO RESPONSÁVEL PELO CONTROLE DE FLUXO
    DAS TELAS DO USUÁRIO

    ====================================================

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 01
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA ALTERAR INFORMAÇÕES PESSOAIS

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 02
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA ENCERRAR CONTA
    '''

    if opcao == 1:
        return_alterar_informacoes = telaAlterarInformacoesPessoais(login)

        if return_alterar_informacoes == True:
            return True

        telaConfiguracoesUsuario(login)

    elif opcao == 2:
        telaEncerrarConta(login)

        telaConfiguracoesUsuario(login)
