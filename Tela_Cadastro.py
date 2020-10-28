from Tela_ConfirmarInformacoes import telaConfirmarInformacoes
from Sistema.InformacoesUsuario import capturarDiretorioUsuario
from Usuario.TratamentoErros import tratarAlpha, tratarNum, tratarCPF

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
    nome = ''
    idade = ''
    login = ''
    senha = ''

    informacoes_usuario = [nome, idade, login, senha]

    for informacao in informacoes_usuario:

        informacao = input(f'{informacao}: ')

        if informacao.islower() == 'sair':
            break


    '''
    CONFIRMA AS INFORMAÇÕES DIGITADAS PELO USUÁRIO
    '''
    return_confirmar = telaConfirmarInformacoes(nome, idade, login, senha)

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