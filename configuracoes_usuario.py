from encerrar_conta import telaEncerrarConta
from tratamento import tratarNum, tratarOpcao
from alterar_informacoes_pessoais import telaAlterarInformacoesPessoais

import os

def telaConfiguracoesUsuario():

    os.system('cls')

    print('\nBANCO WTIC - [CONFIGURAÇÕES DO USUÁRIO]\n')

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

            controleConfiguracoesUsuario(resp)

    telaConfiguracoesUsuario()


def controleConfiguracoesUsuario(opcao):

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
        return_informacoes_pessoais = telaAlterarInformacoesPessoais()

    elif opcao == 2:
        return_encerrar_conta = telaEncerrarConta()