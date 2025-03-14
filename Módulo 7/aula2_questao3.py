import re

def eh_palindromo(frase):
    # Removendo espaços, caracteres especiais e transformando tudo para minúsculas
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    
    # Comparando a string com a sua versão invertida
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ').strip()
    
    if frase.lower() == "fim":
        break  # Encerra o loop se o usuário digitar "fim"

    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
