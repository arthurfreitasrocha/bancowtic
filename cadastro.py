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


    return_capturar_informacoes = capturarInformacoesCadastro()

    if return_capturar_informacoes == False:
        return False


    nome = return_capturar_informacoes[0]
    idade = return_capturar_informacoes[1]
    login = return_capturar_informacoes[2]
    senha = return_capturar_informacoes[3]

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


def capturarInformacoesCadastro():

    '''
    CAPTURA AS INFORMAÇÕES NECESSÁRIAS PARA
    SER REALIZADO O CADASTRO DO USUÁRIO
    '''

    nome = input('NOME: ')

    if nome.lower() == 'sair':
        return False

    else:
        return_validacao = tratarAlpha(nome)

        if return_validacao == False:
            telaCadastro()

    idade = input('IDADE: ')

    if idade.lower() == 'sair':
        return False

    else:
        return_validacao = tratarNum(idade, idade=True)

        if return_validacao == False:
            telaCadastro()

    login = input('CPF (será seu login): ')

    if login.lower() == 'sair':
        return False
    
    else:
        return_validacao = tratarCPF(login)

        if return_validacao == False:
            telaCadastro()

    senha = input('SENHA: ')

    if senha.lower() == 'sair':
        return False


    informacoes = [nome, idade, login, senha]

    return informacoes


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

    informacoes_genericas = ['nome', 'idade', 'saldo', 'extrato', 'login', 'senha']
    informacoes_usuario = [nome, idade, '0', '', login, senha]

    contador = 0
    for informacao in informacoes_usuario:

        diretorio_arquivos = capturarDiretorioUsuario(login)
        diretorio_arquivos += f'\\{informacoes_genericas[contador]}.txt' # 'C:\Users\arthu\Documents\GitHub\bancowtic\usuarios\123\nome.txt'

        arquivo = open(diretorio_arquivos, 'w')
        arquivo.write(informacao)
        arquivo.close()

        contador += 1


    return True