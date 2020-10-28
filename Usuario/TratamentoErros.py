import os


def tratarAlpha(alpha):

    '''
    VERIFICA SE A STRING PASSADA ESTÁ ENTRE OS CARACTERES DO ALFABETO
    '''

    if alpha.isalpha() == False:
        print('\nPOR FAVOR INFORME UMA RESPOSTA VÁLIDA!\n')
        os.system('pause')

        return False

    return True


def tratarNum(num, **kws):

    '''
    VERIFICA SE O VALOR INFORMADO É NUMÉRICO E RETORNA ESSA VALIDAÇÃO COM TRUE OU FALSE

    **kws: idade
    '''

    idade = kws.get('idade')

    if num.isnumeric() == False:
        print('\nPOR FAVOR INFORME UM VALOR NUMÉRICO!\n')
        os.system('pause')

        return False


    if idade == True:

        num = int(num)

        if num < 18:
            print('\nIDADE INVÁLIDA\n')
            os.system('pause')

            return False

    return True


def tratarCPF(cpf):
    
    '''
    VERIFICA SE O CPF É VÁLIDO (INCOMPLETO)
    '''

    if cpf.isalpha() == True:
        print('\nPOR FAVOR INFORME UM CPF VÁLIDO!\n')
        os.system('pause')

        return False

    return True


def tratarOpcao(opcao_escolhida, *opcoes_disponiveis):

    '''
    VERIFICA SE O VALOR INFORMADO ESTÁ DENTRO DAS OPÇÕES DISPONÍVEIS
    '''

    opcao_existente = False
    for opcao in opcoes_disponiveis:

        if opcao == opcao_escolhida:
            opcao_existente = True

    
    if opcao_existente == False:
        print(f'\nPOR FAVOR INFORME UMA OPCAO ENTRE ({opcoes_disponiveis[0]}) E ({opcoes_disponiveis[-1]})!\n')
        os.system('pause')

        return False

    return True