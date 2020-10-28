import os

def telaValidarLogin(**kws):

    '''
    FAZ A VALIDAÇÃO DO LOGIN
    '''

    primeiro_acesso = kws.get('primeiro_acesso')

    os.system('cls')

    print('\nBANCO WTIC - [VALIDAÇÃO]\n')

    print('POR FAVOR INFORME OS DADOS ABAIXO OU DIGITE "sair" PARA SAIR\n')

    login = input('LOGIN: ')

    if login.lower() == 'sair':
        return False

    senha = input('SENHA: ')

    if senha.lower() == 'sair':
        return False


    '''
    PARTE LÓGICA DA VALIDAÇÃO DO LOGIN
    '''
    return_validar_login = controleValidarLogin(login, senha, primeiro_acesso=primeiro_acesso)

    return return_validar_login


def controleValidarLogin(login, senha, **kws):

    '''
    FAZ A VALIDAÇÃO DO LOGIN
    '''

    primeiro_acesso = kws.get('primeiro_acesso')


    todos_usuarios = os.listdir('Banco de Dados\\Usuarios')

    '''
    VERIFICA SE O USUÁRIO EXISTE BASEADO NA PASTA DO MESMO, OU SEJA,
    CASO A PASTA DO USUÁRIO EXISTIR, O USUÁRIO EXISTE
    '''
    usuario_existente = False
    for usuario in todos_usuarios:

        if usuario == login:
            usuario_existente = True


    if usuario_existente == True:

        endereco_login = f'Banco de Dados\\Usuarios\\{login}\\login.txt'
        endereco_senha = f'Banco de Dados\\Usuarios\\{login}\\senha.txt'
        
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

            print('\nAUTENTICAÇÃO REALIZADA COM SUCESSO!\n')
            os.system('pause')

            if primeiro_acesso == True:

                informacoes = [True, login]
                return informacoes

            else:
                return True
        
        else:

            print('\nFALHA NA AUTENTICAÇÃO\n')
            os.system('pause')

            if primeiro_acesso == True:

                informacoes = [False, login]
                return informacoes
            
            else:
                return False

    else:

        print('\nFALHA NA AUTENTICAÇÃO\n')
        os.system('pause')

        if primeiro_acesso == True:

            informacoes = [False, login]
            return informacoes
        
        else:
            return False