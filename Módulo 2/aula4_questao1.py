# Solicita ao usuário o comprimento e a largura do terreno (inteiros)
comprimento = int(input("Digite o comprimento do terreno (m): "))
largura = int(input("Digite a largura do terreno (m): "))

# Solicita o preço do metro quadrado (ponto flutuante)
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

# Calcula a área do terreno
area_m2 = comprimento * largura

# Calcula o valor total do terreno
preco_total = preco_m2 * area_m2

# Exibindo  o resultado formatado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")