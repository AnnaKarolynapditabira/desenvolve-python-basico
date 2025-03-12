import random

# Gerar lista com 20 valores aleatórios entre -100 e 100
lista = [random.randint(-100, 100) for _ in range(20)]

# Ordenar a lista sem modificar a original
lista_ordenada = sorted(lista)

# Índices do maior e menor valor
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

# Exibir resultados
print("Lista ordenada (sem modificar original):", lista_ordenada)
print("Lista original:", lista)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
