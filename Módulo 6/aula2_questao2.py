import random

# Gerar número aleatório entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerar lista com valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Cálculo da soma e média
soma = sum(elementos)
media = soma / num_elementos

# Exibir resultados
print("Lista elementos:", elementos)
print("Soma dos valores:", soma)
print(f"Média dos valores: {media:.2f}")
