import random

def encrypt(nomes):
    n = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
    nomes_criptografados = []

    for nome in nomes:
        nome_criptografado = ''.join(chr(ord(c) + n) for c in nome)
        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, n

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')  # Removendo pontos e traço
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"

    # Cálculo do primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = soma1 % 11
    digito1 = 0 if resto1 < 2 else 11 - resto1

    soma2 = sum(int(cpf[i]) * (10 - i) for i in range(9)) + digito1 * 2
    resto2 = soma2 % 11
    digito2 = 0 if resto2 < 2 else 11 - resto2

    return "Válido" if cpf[-2:] == f"{digito1}{digito2}" else "Inválido"


# Testando a função encrypt
nomes = ["Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)

print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")

# Testando validador de CPF
cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
print("Válido" if validar_cpf(cpf) == "Válido" else "Inválido")
