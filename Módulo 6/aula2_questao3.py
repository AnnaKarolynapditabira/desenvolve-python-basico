import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Encontrar a interseção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

# Contagem de ocorrências em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Exibir listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista Interseção ordenada:", interseccao)

# Exibir contagem de elementos repetidos
print("Contagem:")
for num in interseccao:
    print(f"{num}: (lista1={contagem_lista1[num]}, lista2={contagem_lista2[num]})")
