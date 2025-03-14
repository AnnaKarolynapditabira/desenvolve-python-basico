def encontrar_anagramas(frase, palavra):
    from itertools import permutations

    # Gerar todas as permutações possíveis da palavra
    perms = {''.join(p) for p in permutations(palavra)}
    
    # Separar a frase em palavras
    palavras = frase.split()

    # Filtrar as palavras que são anagramas da palavra objetivo
    anagramas = [p for p in palavras if p in perms]

    return anagramas

# Entrada do usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Encontra e exibe os anagramas
resultado = encontrar_anagramas(frase, palavra_objetivo)
print(f"Anagramas: {resultado}")
