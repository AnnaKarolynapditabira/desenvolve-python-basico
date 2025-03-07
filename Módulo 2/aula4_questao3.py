# Solicita os dados do primeiro produto
produto1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

# Solicita os dados do segundo produto
produto2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

# Solicita os dados do terceiro produto
produto3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o preço total da compra
total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)

# Exibe o resultado formatado com separador de milhar
print(f"Total: R${total:,.2f}")