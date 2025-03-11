# Questão 3
# Description: Jogo de adivinhação de número entre 1 e 10. O programa gera um número aleatório e o usuário deve adivinhar qual é o número. O programa informa se o palpite é muito baixo ou muito alto e só termina quando o usuário acerta o número.

import random

numero_secreto = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))

    if palpite < numero_secreto:
        print("Muito baixo, tente novamente!")
    elif palpite > numero_secreto:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero_secreto}.")
        break
