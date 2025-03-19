# Description: Este programa solicita uma frase ao usuário e salva a frase em um arquivo de texto chamado "frase.txt".
import os

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Salva a frase no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém e imprime o caminho do arquivo salvo
caminho_completo = os.path.abspath(nome_arquivo)
print(f"Frase salva em {caminho_completo}")
