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


def calcula_pontos_regra_simples (lista_int):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for n in lista_int:

        if n ==1 and 1 not in dic:
            dic[1] = 1
        elif n == 1 and 1 in dic:
            dic[1] += 1


        elif n == 2 and 2 not in dic:
            dic[2] = 2
        elif n == 2 and 2 in dic:
            dic[2] += 2


        elif n == 3 and 3 not in dic:
            dic[3] = 3
        elif n == 3 and 3 in dic:
            dic[3] += 3


        elif n == 4 and 4 not in dic:
            dic[4] = 4
        elif n == 4 and 4 in dic:
            dic[4] += 4


        elif n == 5 and 5 not in dic:
            dic[5] = 5
        elif n == 5 and 5 in dic:
            dic[5] += 5


        elif n == 6 and 6 not in dic:
            dic[6] = 6
        elif n == 6 and 6 in dic:
            dic[6] += 6  

    return dic

# print(calcula_pontos_regra_simples([2, 3, 4, 5, 2]))


def calcula_pontos_soma(faces_roladas):
    soma = 0
    for face in faces_roladas:
        soma += face
    return soma


def calcula_pontos_sequencia_baixa(faces_roladas):
    
    if (1 in faces_roladas and
        2 in faces_roladas and
        3 in faces_roladas and
        4 in faces_roladas):
        return 15

    if (2 in faces_roladas and
        3 in faces_roladas and
        4 in faces_roladas and
        5 in faces_roladas):
        return 15

    if (3 in faces_roladas and
        4 in faces_roladas and
        5 in faces_roladas and
        6 in faces_roladas):
        return 15

    return 0



# def calcula_pontos_sequencia_baixa (faces_roladas):
#     eh_sequencia = False
#     for i in range(len(faces_roladas) - 1):
#         if faces_roladas[i+1] == faces_roladas[i] + 1:
#             eh_sequencia = True
#         else:   
#             eh_sequencia = False
#     if eh_sequencia:
#         return 15
#     else:
#         return 0


# print(calcula_pontos_sequencia_baixa([2, 3, 4, 6, 2]))




def calcula_pontos_sequencia_alta(faces_roladas):
    if (1 in faces_roladas and
        2 in faces_roladas and
        3 in faces_roladas and
        4 in faces_roladas and
        5 in faces_roladas):
        return 30
    
    if (2 in faces_roladas and
        3 in faces_roladas and
        4 in faces_roladas and
        5 in faces_roladas and
        6 in faces_roladas):
        return 30
    
    return 0





def calcula_pontos_full_house(faces_roladas):

    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for face in faces_roladas:
        dic[face] += 1

    tem_3 = False
    tem_2 = False

    for valor in dic:
        if dic[valor] == 3:
            tem_3 = True
        if dic[valor] == 2:
            tem_2 = True

    if tem_3 and tem_2:
        return calcula_pontos_soma(faces_roladas)
    
    return 0




def calcula_pontos_quadra(faces_roladas):

    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for face in faces_roladas:
        dic[face] += 1

    for valor in dic:
        if dic[valor] >= 4:
            return calcula_pontos_soma(faces_roladas)

    return 0



def calcula_pontos_quina(faces_roladas):
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for face in faces_roladas:
        dic[face] += 1

    for face in dic:
        if dic[face] >= 5:
            return 50

    return 0