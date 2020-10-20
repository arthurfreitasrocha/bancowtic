from diretorio_atual import capturarDiretorioAtual

import os

def validarLogin(login, senha):

    '''
    FAZ A VALIDAÇÃO DO LOGIN
    '''

    diretorio_atual = capturarDiretorioAtual()
    diretorio_usuarios = f'{diretorio_atual}\\usuarios'

    usuarios = os.listdir(diretorio_usuarios)


    '''
    VERIFICA SE O USUÁRIO EXISTE BASEADO NA PASTA DO MESMO, OU SEJA,
    CASO A PASTA DO USUÁRIO EXISTIR, O USUÁRIO EXISTE
    '''
    usuario_existente = False
    for usuario in usuarios:

        if usuario == login:
            usuario_existente = True


    if usuario_existente == True:

        endereco_login = f'{diretorio_usuarios}\\{login}\\login.txt'
        endereco_senha = f'{diretorio_usuarios}\\{login}\\senha.txt'
        
        arquivo = open(endereco_login, 'r')
        login_arquivo = arquivo.read()
        arquivo.close()

        arquivo = open(endereco_senha, 'r')
        senha_arquivo = arquivo.read()
        arquivo.close()


        '''
        SE O LOGIN INFORMADO NÃO COINCIDIR COM OS DADOS NO
        BANCO DE DADOS OCORRERÁ A FALHA NO LOGIN
        '''
        if login_arquivo == login and senha_arquivo == senha:
            return True
        
        else:
            return False

    else:
        print('aaaaaaa')
        return False