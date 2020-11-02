

def escreverArquivo(local, string=''):

    arquivo = open(local, 'w')
    arquivo.write(string)
    arquivo.close()


def lerArquivo(local):

    arquivo = open(local, 'r')
    conteudo_arquivo = arquivo.read()
    arquivo.close()

    return conteudo_arquivo


def acrescentarTextoArquivo(local, string):

    arquivo = open(local, 'a')
    arquivo.write(string)
    arquivo.close()
