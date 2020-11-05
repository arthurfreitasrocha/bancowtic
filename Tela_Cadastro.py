from Tela_ConfirmarInformacoes import telaConfirmarInformacoes

import os

def telaCadastro():

    '''
    EXIBE A TELA DE CADASTRO
    '''

    os.system('cls')

    print('\nBANCO WTIC - [CADASTRO]\n')

    print('POR FAVOR INFORME OS DADOS ABAIXO OU DIGITE "sair" PARA SAIR\n')


    '''
    CAPTURA AS INFORMAÇÕES
    '''

    variaveis_informacoes = []

    for informacao in ['nome', 'idade', 'login', 'senha']:

        nova_informacao = input(f'{informacao.upper()}: ')

        if nova_informacao.lower() == 'sair':
            return False

        variaveis_informacoes.append(nova_informacao)


    '''
    ATRIBUI A INFORMAÇÃO DIGITADA PELO USUÁRIO
    AS VARIÁVEIS
    '''
    nome = variaveis_informacoes[0]
    idade = variaveis_informacoes[1]
    login = variaveis_informacoes[2]
    senha = variaveis_informacoes[3]


    '''
    CONFIRMA AS INFORMAÇÕES DIGITADAS PELO USUÁRIO
    '''
    return_confirmar = telaConfirmarInformacoes(nome, idade, login, senha)


    if return_confirmar == True:

        return_cadastro = cadastrarUsuario(nome, idade, login, senha)

        if return_cadastro == True:
            print('\nCADASTRO REALIZADO COM SUCESSO!\n')
            os.system('pause')

        elif return_cadastro == False:
            print('\nVERIFIQUE SEUS DADOS E TENTE NOVAMENTE\n')
            os.system('pause')

            telaCadastro()

    else:
        telaCadastro()


def cadastrarUsuario(nome, idade, login, senha):

    '''
    CRIA O BANCO DE DADOS DO USUÁRIO
    '''


    '''
    VERIFICA SE O USUÁRIO QUE ESTÁ TENTANDO SE CADASTRAR
    JÁ EXISTE NO BANCO DE DADOS
    '''

    todos_usuarios = os.listdir('Banco de Dados\\Usuarios')

    usuario_existente = False
    for usuario in todos_usuarios:

        if usuario == login:
            usuario_existente = True

    if usuario_existente == True:
        return False


    '''
    CRIA A PASTA DO USUÁRIO, E DENTRO DELA ESTARÃO SUAS
    INFORMAÇÕES ESCRITAS EM VÁRIOS BLOCOS DE NOTAS
    '''

    os.mkdir(f'Banco de Dados\\Usuarios\\{login}')
    variaveis_informacoes = [nome, idade, '0', '', login, senha]

    contador = 0 #1
    for informacao in ['nome', 'idade', 'saldo', 'extrato', 'login', 'senha']:

        diretorio_usuario = f'Banco de Dados\\Usuarios\\{login}\\{informacao}.txt'

        arquivo = open(diretorio_usuario, 'w')
        arquivo.write(variaveis_informacoes[contador])
        arquivo.close()

        contador += 1


    return True