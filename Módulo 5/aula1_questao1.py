# Title: Questão 1
# Description: Faça um programa que leia dois números e imprima a diferença absoluta entre eles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

diferenca = round(abs(num1 - num2), 2)

print(f"A diferença absoluta entre os números é: {diferenca}")
