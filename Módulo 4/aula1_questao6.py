# Lendo o número de experimentos
N = int(input())

# Inicializando contadores
total = 0
coelhos = 0
ratos = 0
sapos = 0

# Processando cada experimento
for _ in range(N):
    entrada = input().split()  # Lê a entrada e separa os valores
    quantidade = int(entrada[0])
    tipo = entrada[1]

    # Atualizando os contadores conforme o tipo da cobaia
    total += quantidade
    if tipo == 'C':
        coelhos += quantidade
    elif tipo == 'R':
        ratos += quantidade
    elif tipo == 'S':
        sapos += quantidade

# Calculando percentuais
percentual_coelhos = (coelhos / total) * 100 if total > 0 else 0
percentual_ratos = (ratos / total) * 100 if total > 0 else 0
percentual_sapos = (sapos / total) * 100 if total > 0 else 0

# Exibindo os resultados formatados
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
