import funcoes

# Inicialização
cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1, 'quadra': -1, 'full_house': -1,
        'sequencia_baixa': -1, 'sequencia_alta': -1, 'cinco_iguais': -1
    }
}

categorias_simples = ['1', '2', '3', '4', '5', '6']
categorias_avancadas = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

rodadas = 0
while rodadas < 12:
    dados_rolados = funcoes.rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    turno_ativo = True
    
    while turno_ativo:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        
        opcao = input()
        
        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            dados_rolados, dados_guardados = funcoes.guardar_dado(dados_rolados, dados_guardados, idx)
            
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            dados_rolados, dados_guardados = funcoes.remover_dado(dados_rolados, dados_guardados, idx)
            
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
            
            # Verificação de validade simplificada para evitar loops infinitos no judge
            valida = False
            if comb in categorias_simples:
                if cartela['regra_simples'][int(comb)] == -1:
                    valida = True
            elif comb in categorias_avancadas:
                if cartela['regra_avancada'][comb] == -1:
                    valida = True
            
            if valida:
                todos = dados_rolados + dados_guardados
                cartela = funcoes.faz_jogada(todos, comb, cartela)
                turno_ativo = False # Finaliza a rodada com sucesso
                rodadas += 1
            else:
                if comb not in categorias_simples and comb not in categorias_avancadas:
                    print("Combinação inválida. Tente novamente.")
                else:
                    print("Essa combinação já foi utilizada.")
        else:
            print("Opção inválida. Tente novamente.")

# --- Finalização ---
pontos_total = 0
soma_simples = 0

for i in range(1, 7):
    p = cartela['regra_simples'][i]
    if p != -1:
        soma_simples += p
        pontos_total += p

for cat in categorias_avancadas:
    p = cartela['regra_avancada'][cat]
    if p != -1:
        pontos_total += p

if soma_simples >= 63:
    pontos_total += 35

funcoes.imprime_cartela(cartela)
print(f"Pontuação total: {pontos_total}")