from confirmar_informacoes import telaConfirmarInformacoes
from diretorio_atual import capturarDiretorioAtual
from tratamento import tratarAlpha, tratarNum, tratarCPF

import os

def telaCadastro():

    '''
    EXIBE A TELA DE CADASTRO
    '''

    os.system('cls')

    print('\nBANCO WTIC - [CADASTRO]\n')

    print('POR FAVOR INFORME OS DADOS ABAIXO OU DIGITE "sair" PARA SAIR\n')


    nome = input('NOME: ')

    if nome.lower() == 'sair':
        return False

    else:
        return_validacao = validarInformacoes('nome', nome)

        if return_validacao == False:
            telaCadastro()

    idade = input('IDADE: ')

    if idade.lower() == 'sair':
        return False

    else:
        return_validacao = validarInformacoes('idade', idade)

        if return_validacao == False:
            telaCadastro()

    login = input('CPF (será seu login): ')

    if login.lower() == 'sair':
        return False
    
    else:
        return_validacao = validarInformacoes('cpf', login)

        if return_validacao == False:
            telaCadastro()

    senha = input('SENHA: ')

    if senha.lower() == 'sair':
        return False


    return_confirmar = telaConfirmarInformacoes('cadastro', login, senha, nome=nome, idade=idade)

    if return_confirmar == True:
        return_cadastro = cadastrarUsuario(nome, idade, login, senha)

        if return_cadastro == True:
            print('\nCADASTRO REALIZADO COM SUCESSO!\n')
            os.system('pause')

            return True

        elif return_cadastro == False:
            print('\nVERIFIQUE SEUS DADOS E TENTE NOVAMENTE\n')
            os.system('pause')

            telaCadastro()

    else:
        telaCadastro()


def validarInformacoes(tipo_informacao, informacao):

    return_informacao = False

    if tipo_informacao == 'nome':
        return_informacao = tratarAlpha(informacao)

        return return_informacao


    elif tipo_informacao == 'idade':
        return_informacao = tratarNum(informacao)

        if return_informacao == True:

            informacao = int(informacao)

            if informacao < 18:
                return_informacao = False


    elif tipo_informacao == 'cpf':
        return_informacao = tratarCPF(informacao)

        return return_informacao


    if return_informacao == False:
        print('\nENTRADA INVÁLIADA!\n')
        os.system('pause')

        return False


def cadastrarUsuario(nome, idade, login, senha):

    '''
    CRIA O BANCO DE DADOS DO USUÁRIO
    '''

    diretorio_atual = capturarDiretorioAtual()
    diretorio_usuarios = f'{diretorio_atual}\\usuarios'

    usuarios = os.listdir(diretorio_usuarios)


    usuario_existente = False
    for usuario in usuarios:

        if usuario == login:
            usuario_existente = True


    if usuario_existente == True:
        return False


    pasta_usuario = f'{diretorio_usuarios}\\{login}'
    os.mkdir(pasta_usuario)

    informacoes_genericas = ['nome', 'idade', 'login', 'senha']
    informacoes_usuario = [nome, idade, login, senha]

    contador = 0
    for informacao in informacoes_usuario:

        diretorio_arquivos = f'{diretorio_usuarios}\\{login}\\{informacoes_genericas[contador]}.txt'

        arquivo = open(diretorio_arquivos, 'w')
        arquivo.write(informacao)
        arquivo.close()

        contador += 1


    return True