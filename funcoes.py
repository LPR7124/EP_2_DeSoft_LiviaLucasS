import random
def rolar_dados(n):
    i = 0
    lista_dados = []
    while i<n:
        dado = random.randint(1,6)
        lista_dados.append(dado)
        i += 1
    return lista_dados

def guardar_dado (dados_rolados, dados_guardados, índice):
    if índice < len(dados_rolados):
        dado = dados_rolados[índice]
        dados_guardados.append(dado)
        dados_rolados = dados_rolados[:índice] + dados_rolados[índice+1:] # pega o elemento antes do índice e o elemento depois do próximo da  lista(retira assim o que tem o indice indicado na lista)

    return [dados_rolados, dados_guardados]

# dados_rolados = [1, 3, 2]
# dados_no_estoque = [1, 2]
# dado_para_guardar = 1

# print(guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar))


def remover_dado(dados_rolados, dados_guardados, índice):
    if índice < len(dados_guardados):
        dado = dados_guardados[índice]
        dados_rolados.append(dado)
        dados_guardados = dados_guardados[:índice] + dados_guardados[índice+1:]

    return [dados_rolados, dados_guardados]



# dados_rolados = [2, 2, 2, 2]
# dados_no_estoque = [1]
# dado_para_remover = 0

# print(remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))
