# Lista de números pares entre 20 e 50
pares = [num for num in range(20, 51, 2)]
print("Pares entre 20 e 50:", pares)

# Quadrados dos valores de 1 a 9
quadrados = [num**2 for num in range(1, 10)]
print("Quadrados de 1 a 9:", quadrados)

# Números entre 1 e 100 divisíveis por 7
div7 = [num for num in range(1, 101) if num % 7 == 0]
print("Divisíveis por 7 entre 1 e 100:", div7)

# Paridade dos números em range(0,30,3)
paridade = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print("Paridade dos valores:", paridade)
