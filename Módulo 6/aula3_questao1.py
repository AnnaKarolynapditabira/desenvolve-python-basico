# Entrada de números do usuário
numeros = []
while len(numeros) < 4:  # Garante que pelo menos 4 números sejam inseridos
    try:
        num = int(input("Digite um número inteiro (ou qualquer outra tecla para parar): "))
        numeros.append(num)
    except ValueError:
        break  # Para quando a entrada não for um número

# Exibição dos diferentes fatiamentos
print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
