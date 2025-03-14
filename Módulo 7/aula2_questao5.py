import random

def embaralhar_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras
    frase_embaralhada = []

    for palavra in palavras:
        if len(palavra) > 3:  # Só embaralha palavras com mais de 3 caracteres
            # Mantém o primeiro e o último caractere, embaralha o meio
            inicio = palavra[0]
            fim = palavra[-1]
            meio = list(palavra[1:-1])  # Pega os caracteres internos
            random.shuffle(meio)  # Embaralha os caracteres internos
            palavra_embaralhada = inicio + ''.join(meio) + fim
        else:
            palavra_embaralhada = palavra  # Palavras com 3 ou menos caracteres não são embaralhadas

        frase_embaralhada.append(palavra_embaralhada)

    return ' '.join(frase_embaralhada)  # Junta as palavras de volta em uma frase

# Solicita ao usuário que digite uma frase
frase_usuario = input("Digite uma frase para embaralhar as palavras: ")

# Chama a função e exibe o resultado
resultado = embaralhar_palavras(frase_usuario)
print("\nFrase embaralhada:", resultado)
