def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    tamanho_min = min(len(lista1), len(lista2))

    # Intercalando até o final da menor lista
    for i in range(tamanho_min):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

    # Adicionando o restante da maior lista
    lista_intercalada.extend(lista1[tamanho_min:])
    lista_intercalada.extend(lista2[tamanho_min:])

    return lista_intercalada

# Entrada da primeira lista
tamanho1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input()) for _ in range(tamanho1)]

# Entrada da segunda lista
tamanho2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input()) for _ in range(tamanho2)]

# Gerar lista intercalada
lista_intercalada = intercalar_listas(lista1, lista2)

# Exibir resultado
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
