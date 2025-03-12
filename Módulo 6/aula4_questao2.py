# Entrada do usuário
frase = input("Digite uma frase: ")

# Definição de vogais
vogais = "aeiouAEIOU"

# Extração de vogais e consoantes
lista_vogais = sorted([letra for letra in frase if letra in vogais])
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]

# Exibição dos resultados
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
