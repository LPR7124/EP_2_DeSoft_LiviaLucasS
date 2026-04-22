import random
def rolar_dados(n):
    i = 0
    lista_dados = []
    while i<n:
        dado = random.randint(1,6)
        lista_dados.append(dado)
        i += 1
    return lista_dados

