# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
indices = [i for i, c in enumerate(frase) if c in vogais]

# Exibe a quantidade e os índices das vogais
print(f"{len(indices)} vogais")
print(f"Índices: {indices}")
