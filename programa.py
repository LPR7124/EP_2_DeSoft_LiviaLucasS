import funcoes

# 1. Inicialização da Cartela
cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

categorias_simples = ['1', '2', '3', '4', '5', '6']
categorias_avancadas = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

# 2. Loop Principal (12 Rodadas)
rodadas_completas = 0
while rodadas_completas < 12:
    dados_rolados = funcoes.rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    marcou_pontuacao = False
    
    # Loop de ações do jogador dentro da rodada
    while marcou_pontuacao == False:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        
        opcao = input() # O judge espera o input logo após o print
        
        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            resultado = funcoes.guardar_dado(dados_rolados, dados_guardados, idx)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            resultado = funcoes.remover_dado(dados_rolados, dados_guardados, idx)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            
        elif opcao == '3':
            if rerrolagens < 2:
                dados_rolados = funcoes.rolar_dados(len(dados_rolados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")
                
        elif opcao == '4':
            funcoes.imprime_cartela(cartela)
            
        elif opcao == '0':
            print("Digite a combinação desejada:")
            comb = input()
            
            # Validação se a combinação existe
            existe = False
            if comb in categorias_simples or comb in categorias_avancadas:
                existe = True
            
            if existe == False:
                print("Combinação inválida. Tente novamente.")
            else:
                # Verificação se a combinação já foi usada
                ja_foi = False
                if comb in categorias_simples:
                    if cartela['regra_simples'][int(comb)] != -1:
                        ja_foi = True
                else:
                    if cartela['regra_avancada'][comb] != -1:
                        ja_foi = True
                
                if ja_foi:
                    print("Essa combinação já foi utilizada.")
                else:
                    # Se chegou aqui, a jogada é válida!
                    todos_dados = dados_rolados + dados_guardados
                    cartela = funcoes.faz_jogada(todos_dados, comb, cartela)
                    marcou_pontuacao = True 
        else:
            print("Opção inválida. Tente novamente.")

    rodadas_completas += 1

# 3. Finalização e Bônus
pontuacao_total = 0
soma_regra_simples = 0

# Somar categorias simples
for i in range(1, 7):
    pts = cartela['regra_simples'][i]
    if pts != -1:
        soma_regra_simples += pts
        pontuacao_total += pts

# Somar categorias avançadas
for cat in categorias_avancadas:
    pts = cartela['regra_avancada'][cat]
    if pts != -1:
        pontuacao_total += pts

# Aplicar bônus de engenheiro (se soma simples >= 63)
if soma_regra_simples >= 63:
    pontuacao_total += 35

# Impressão Final
funcoes.imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")