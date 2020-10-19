from confirmar_informacoes import telaConfirmarInformacoes
from diretorio_atual import capturarDiretorioAtual, capturarDiretorioUsuario
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

    '''
    VERIFICA SE A PASTA "usuarios" JA FOI CRIADA
    '''

    arquivos_no_diretorio = os.listdir(diretorio_atual)

    pasta_usuario_existe = False
    for nome_arquivos in arquivos_no_diretorio:

        if nome_arquivos == 'usuarios':
            pasta_usuario_existe = True

    if pasta_usuario_existe == False:
        os.mkdir('usuarios')


    diretorio_pasta_usuarios = f'{diretorio_atual}\\usuarios'
    usuarios = os.listdir(diretorio_pasta_usuarios)


    '''
    VERIFICA SE O USUÁRIO QUE ESTÁ TENTANDO SE CADASTRAR
    JÁ EXISTE NO BANCO DE DADOS
    '''

    usuario_existente = False
    for usuario in usuarios:

        if usuario == login:
            usuario_existente = True

    if usuario_existente == True:
        return False


    '''
    CRIA A PASTA DO USUÁRIO, E DENTRO DELA ESTARÃO SUAS
    INFORMAÇÕES ESCRITAS EM VÁRIOS BLOCOS DE NOTAS
    '''

    pasta_usuario = capturarDiretorioUsuario(login)
    os.mkdir(pasta_usuario)

    informacoes_genericas = ['nome', 'idade', 'login', 'senha']
    informacoes_usuario = [nome, idade, login, senha]

    contador = 0
    for informacao in informacoes_usuario:

        diretorio_arquivos = capturarDiretorioUsuario(login)
        diretorio_arquivos += f'\\{informacoes_genericas[contador]}.txt' # 'C:\Users\arthu\Documents\GitHub\bancowtic\usuarios\123\nome.txt'

        arquivo = open(diretorio_arquivos, 'w')
        arquivo.write(informacao)
        arquivo.close()

        contador += 1


    return True