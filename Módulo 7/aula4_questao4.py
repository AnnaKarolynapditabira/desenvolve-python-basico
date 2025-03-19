# aula4_questao4.py
import random

# Ler palavras do arquivo
with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = [linha.strip() for linha in arquivo.readlines()]

# Escolher palavra aleatoriamente
palavra = random.choice(palavras).lower()
tentativas = 6
letras_certas = ["_"] * len(palavra)

# Carregar estágios do enforcado
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
    estagios = arquivo.read().split("\n\n")

def imprime_enforcado(erros):
    print(estagios[erros])

erros = 0
while erros < tentativas and "_" in letras_certas:
    print(" ".join(letras_certas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                letras_certas[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

if "_" not in letras_certas:
    print("Parabéns, você venceu!")
else:
    print(f"Você perdeu! A palavra era '{palavra}'.")