# aula4_questao3.py
import re

# Abrir o arquivo "estomago.txt" para leitura
with open("estomago.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Exibir as primeiras 25 linhas
print("Primeiras 25 linhas do arquivo:\n")
print("".join(linhas[:25]))

# Contar número total de linhas
print(f"\nNúmero total de linhas: {len(linhas)}")

# Encontrar a linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print("\nLinha com maior número de caracteres:\n", linha_maior.strip())

# Contar menções aos nomes "Nonato" e "Íria"
count_nonato = sum(len(re.findall(r'\b[Nn]onato\b', linha)) for linha in linhas)
count_iria = sum(len(re.findall(r'\b[Ii]ría\b', linha)) for linha in linhas)

print(f"\nMenções a 'Nonato': {count_nonato}")
print(f"Menções a 'Íria': {count_iria}")