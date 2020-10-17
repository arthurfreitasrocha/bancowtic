from operacoes_bancarias import telaOperacoesBancarias
from configuracoes_usuario import telaConfiguracoesUsuario

from diretorio_atual import capturarDiretorioUsuario
from tratamento import tratarNum, tratarOpcao
from sair import sairBanco

import os

def telaUsuario(login):

    informacoes_usuario = capturarInformacoesUsuario(login)

    nome = informacoes_usuario[0]
    idade = informacoes_usuario[1]

    os.system('cls')

    print(f'\nBANCO WTIC - [TELA USUÁRIO] - BEM-VINDO ({nome.title()})!\n')

    print('POR FAVOR SELECIONE UMA OPÇÃO OU DIGITE "sair" PARA SAIR\n')

    print('(01) OPERAÇÕES BANCÁRIAS')
    print('(02) CONFIGURAÇÕES DO USUÁRIO\n')

    resp = input('>>> ')

    if resp.lower() == 'sair':
        return False

    return_tratamento = tratarNum(resp)


    '''
    PARTE LÓGICA DA TELA USUÁRIO
    '''
    if return_tratamento == True:

        resp = int(resp)
        return_tratamento = tratarOpcao(resp, 1,2)

        if return_tratamento == True:

            controleUsuario(login)


def capturarInformacoesUsuario(login):

    '''
    ESSA FUNÇÃO É RESPONSÁVEL POR CAPTURAR
    AS INFORMAÇÕES PESSOAIS DO USUÁRIO (NOME, IDADE)
    '''

    diretorio_usuario = capturarDiretorioUsuario(login)

    nome_arquivos = ['nome.txt', 'idade.txt']
    informacoes_usuario = []

    for nome_arquivo in nome_arquivos:

        diretorio_arquivo = f'{diretorio_usuario}\\{nome_arquivo}'

        arquivo = open(diretorio_arquivo, 'r')
        informacao = arquivo.read()
        arquivo.close()

        informacoes_usuario.append(informacao)

    return informacoes_usuario


def controleUsuario(login):

    '''
    FUNÇÃO RESPONSÁVEL PELO CONTROLE DE FLUXO
    DAS TELAS DO USUÁRIO

    ====================================================

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 01
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA OPERAÇÕES BANCÁRIAS

    CASO A OPÇÃO ESCOLHIDA SEJA A Nº 02
    O USUÁRIO SERÁ REDIRECIONADO PARA A TELA CONFIGURAÇÕES DO USUÁRIO
    '''

    return_usuario = telaUsuario(login)

    if return_usuario == False:
        sairBanco()

    elif return_usuario == 1:
        return_operacoes = telaOperacoesBancarias()

    elif return_usuario == 2:
        return_configuracoes = telaConfiguracoesUsuario()
