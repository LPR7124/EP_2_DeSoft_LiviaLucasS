import funcoes

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

rodada = 0
while rodada < 12:
    dados_rolados = funcoes.rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    fez_jogada_na_rodada = False
    
    while fez_jogada_na_rodada == False:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        
        opcao = input(">")
        
        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input(">"))
            resultado = funcoes.guardar_dado(dados_rolados, dados_guardados, idx)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input(">"))
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
            comb = input(">")
            
            # Validação manual de categoria
            valida = False
            if comb in categorias_simples or comb in categorias_avancadas:
                valida = True
            
            if valida == False:
                print("Combinação inválida. Tente novamente.")
            else:
                # Verificação se já foi preenchido
                ocupado = False
                if comb in categorias_simples:
                    if cartela['regra_simples'][int(comb)] != -1:
                        ocupado = True
                else:
                    if cartela['regra_avancada'][comb] != -1:
                        ocupado = True
                
                if ocupado:
                    print("Essa combinação já foi utilizada.")
                else:
                    # Une os dados para calcular a pontuação final da rodada
                    todos_dados = dados_rolados + dados_guardados
                    cartela = funcoes.faz_jogada(todos_dados, comb, cartela)
                    fez_jogada_na_rodada = True # Sai do loop da rodada
        else:
            print("Opção inválida. Tente novamente.")
            
    rodada += 1

# --- Cálculo Final ---
pontuacao_total = 0
soma_simples = 0

# Soma Regra Simples
for i in range(1, 7):
    ponto = cartela['regra_simples'][i]
    if ponto != -1:
        soma_simples += ponto
        pontuacao_total += ponto

# Soma Regra Avançada
for chave in categorias_avancadas:
    ponto = cartela['regra_avancada'][chave]
    if ponto != -1:
        pontuacao_total += ponto

if soma_simples >= 63:
    pontuacao_total += 35

funcoes.imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")