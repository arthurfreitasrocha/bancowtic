from .Tela_EncerrarConta import telaEncerrarConta
from .TratamentoErros import tratarNum, tratarOpcao
from .Tela_AlterarInformacoesPessoais import telaAlterarInformacoesPessoais

import os

def telaConfiguracoesUsuario(login):

    '''
    EXIBE A TELA DAS CONFIGURAÇÕES DO USUÁRIO
    '''

    os.system('cls')

    print('\nBANCO WTIC - [TELA USUÁRIO -> CONFIGURAÇÕES DO USUÁRIO]\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) ALTERAR INFORMAÇÕES PESSOAIS')
    print('(02) ENCERRAR CONTA\n')

    resp = input('>>> ')
    print(resp)

    if resp.lower() == 'sair':
        print('entrou no if')
        os.system('pause')
        informacoes = [False, login]
        return informacoes

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

        telaConfiguracoesUsuario(return_alterar_informacoes)

    elif opcao == 2:
        telaEncerrarConta(login)

        telaConfiguracoesUsuario(login)
