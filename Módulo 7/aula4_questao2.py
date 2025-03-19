# Description: Escreva um programa que leia o arquivo "frase.txt" e crie um novo arquivo chamado "palavras.txt" contendo uma palavra por linha. O arquivo "palavras.txt" deve conter apenas palavras, sem pontuações ou caracteres especiais. Utilize expressões regulares para remover os caracteres não alfabéticos.
import re

# Lê o arquivo "frase.txt"
with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Remove caracteres não alfabéticos e divide as palavras
palavras = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b', conteudo)

# Salva as palavras no novo arquivo "palavras.txt"
with open("palavras.txt", "w", encoding="utf-8") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Imprime o conteúdo do novo arquivo
with open("palavras.txt", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
