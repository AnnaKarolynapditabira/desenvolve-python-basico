# Solicita os dados ao usuário
distancia = float(input("Digite a distância da entrega (km): "))
peso = float(input("Digite o peso do pacote (kg): "))

# Define o valor do frete por kg de acordo com a distância
if distancia <= 100:
    custo_por_kg = 1.0
elif distancia <= 300:
    custo_por_kg = 1.5
else:
    custo_por_kg = 2.0

# Calcula o valor do frete
frete = custo_por_kg * peso

# Adiciona taxa extra se o peso for superior a 10 kg
if peso > 10:
    frete += 10

# Exibe o valor final do frete
print(f"Valor do frete: R${frete:.2f}")
