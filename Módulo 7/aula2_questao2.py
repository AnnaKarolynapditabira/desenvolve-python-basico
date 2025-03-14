def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    for vogal in vogais:
        frase = frase.replace(vogal, "*")
    return frase

frase = input("Digite uma frase: ")
print("Frase modificada:", substituir_vogais(frase))
