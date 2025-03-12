import random

# Gerar lista aleatória com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

# Encontrar o intervalo com mais números negativos
max_negativos = 0
inicio_intervalo = 0

for i in range(len(lista) - 4):  # Verifica blocos de 5 elementos
    intervalo = lista[i:i+5]
    negativos = sum(1 for num in intervalo if num < 0)

    if negativos > max_negativos:
        max_negativos = negativos
        inicio_intervalo = i

# Remover o intervalo encontrado
del lista[inicio_intervalo:inicio_intervalo+5]

# Exibir lista editada
print("Lista editada:", lista)
