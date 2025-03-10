N = int(input("Digite a quantidade de respondentes: "))
soma_idades = 0

for i in range(N):
    idade = int(input(f"Digite a idade do {i+1}º respondente: "))
    soma_idades += idade

media = soma_idades / N
print(f"Média das idades: {media:.2f}")