# Questão 2 
# Description: Escreva um programa que gere uma quantidade n de números aleatórios e calcule a raiz quadrada da soma desses números.

import random
import math

n = int(input("Digite a quantidade de números aleatórios: "))

soma = sum(random.randint(0, 100) for _ in range(n))
raiz_quadrada = round(math.sqrt(soma), 2)

print(f"A raiz quadrada da soma dos números é: {raiz_quadrada}")
