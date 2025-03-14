numero = input("Digite o número: ")

# Verifica se o número tem 8 dígitos e adiciona '9' na frente, se necessário
if len(numero) == 8:
    numero = '9' + numero

# Formata o número no formato adequado
numero_formatado = f"{numero[:5]}-{numero[5:]}"
print(f"Número completo: {numero}")
