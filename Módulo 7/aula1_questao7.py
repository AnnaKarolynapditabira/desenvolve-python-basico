import random

def encrypt_name(nome, n):
    encrypted = ''.join(chr((ord(c) + n - 32) % 95 + 32) for c in nome)
    return encrypted

def encrypt_names(nomes):
    import random
    chave_aleatoria = random.randint(1, 9)
    nomes_criptografados = [
        ''.join(chr((ord(c) + chave_aleatoria - 32) % 95 + 32) if 32 <= ord(c) <= 126 else c for nome in nomes for c in nome
    ]
    return nomes_criptografados, chave_aleatoria

# Exemplo de uso
nomes = ["Luana", "Juana", "Ju", "Pri"]
nomes_criptografados, chave = encrypt(nomes)
print(f"Chave Aleatória: {chave_aleatoria}")
print("Nomes Criptografados:", nomes_criptografados)